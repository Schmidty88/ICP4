import numpy as numpy
# creating an array that is 10x10
array = numpy.random.random((10,10))
print(array)
# finding the max row
maxRow = 1
print("------Rows Maximum Values---------")
for maxVal in array.max(axis=1):
    print("Row%d max value is : " % maxRow, float(maxVal))
    maxRow += 1
# finding the min row
minRow = 1
print("-------Rows Minimum Values---------")
for minVal in array.min(axis=1):
    print("Row%d min value is : " % minRow, float(minVal))
    minRow += 1
print("-------------------")