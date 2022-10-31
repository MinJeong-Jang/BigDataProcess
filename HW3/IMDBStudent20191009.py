#!/usr/bin/python3

import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

genreDic = dict{}

with open(inputFile, "rt") as fp:
	for line in fp:
		movie = line.split("::")
		genreList = movie[2].strip().split("|")

		for genre in genreList:
			if genre not in countGenre:
				genreDic[genre] = 1
			else:
				genreDic[genre] += 1

with open(outputFile, "at") as fp:
	items = genreDic.items()
	for item in items:
		fp.write(item[0] + " " + str(item[1]) + "\n")
