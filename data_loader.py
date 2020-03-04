#! -*- coding:utf-8 -*-,

import csv

# CSV Reader
def csv2Tuple(path):
    _File = open(path)
    _Reader = csv.reader(_File)
    return tuple(_Reader)

# Data formatter
def dataFormat(inData):
    outData = []
    lineLen = len(inData)
    for i in range(2, lineLen):
        outData.append(tuple(inData[i][1:]))
    return outData