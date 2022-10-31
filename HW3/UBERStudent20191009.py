#!/usr/bin/python3

import sys
import calendar

inputfile = sys.argv[1]
outputfile = sys.argv[2]
dayOfWeek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

uberDic = dict()
with open(inputfile, "rt") as fp:
	for line in fp:
		uber = line.split(",")
		dayList = uber[1].split("/")
		day = calendar.weekday(int(dayList[2]), int(dayList[0]), int(dayList[1]))

		n = uber[0]
		vehicle = int(uber[2])
		trip = int(uber[3][:-1])
		key = n + "," + dayOfWeek[day]

		if key in uberDic:
			value = uberDic[key].split(",")
			vehicle += int(value[0])
			trip += int(value[1])
		uberDic = str(vehicle) + "," + str(trip)

with open(outputfile, "wt") as fp:
	items = uberDic.items()
	for item in items:
		fp.write(item[0] + " " + str(item[1]) + "\n")
