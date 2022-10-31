#!/usr/bin/python3

import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

genreDic = dict()

with open(inputfile, "rt") as fp:
	for line in fp:
		movie = line.split("::")
		genreList = movie[2].strip().split("|")

		for genre in genreList:
			if genre not in genreDic:
				genreDic[genre] = 1
			else:
				genreDic[genre] += 1

with open(outputfile, "wt") as fp:
	items = genreDic.items()
	for item in items:
		fp.write(item[0] + " " + str(item[1]) + "\n")
