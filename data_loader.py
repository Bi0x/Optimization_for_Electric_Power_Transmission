#! -*- coding:utf-8 -*-,

import csv

# CSV Reader
def csv2Tuple(path):
    _File = open(path)
    _Reader = csv.reader(_File)
    return tuple(_Reader)

# Data formatter
def dataFormat(inData):
    