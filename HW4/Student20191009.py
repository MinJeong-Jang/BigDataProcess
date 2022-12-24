#!/usr/bin/python3

import numpy as np
import operator
import sys
import os

def createDataSet(fileDir):
	labels = []
	fileList = listdir(fileDir)
	m = len(fileList)
	trainingMat = np.zeros((m, 1024))

	for i in range(m):
		fileName = fileList[i]
		classNum = int(fileName.split('_')[0])
		labels.append(classNum)
		trainingMat[i, :] = getVector(fileDir +'/' + fileName)

	return labels, trainingMat

def getVector(fileName):
	v = np.zeros((1, 1024))
	
	with open(fileName) as fp:
		for i in range(32):
			l = fp.readline()
			for j in range(32):
				v[0, 32 * i + j] = int(l[j])

		return v

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)

	return sortedClassCount[0][0]

trainingDigits = sys.argv[1]
testDigits = sys.argv[2]
testFiles = listdir(testDigits)
m = len(testFiles)

label, mat = createDataSet(trainingDigits)

for k in range(1, 21):
	errorCount = 0
	count = 0

	for i in range(m):
		answer = int(testFiles[i].split('_')[0])
		data = getVector(testDigits + '/' + testFiles[i])
		result = classify0(data, mat, labels, k)
		count += 1

		if answer != result:
			errorCount += 1
	
	print(int(errorCount / count * 100))
		



