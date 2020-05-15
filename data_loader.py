
import csv
import networkx as nx

# CSV Reader
def csv2Tuple(path):
    _File = open(path)
    _Reader = csv.reader(_File)
    return tuple(_Reader)

# Data formatter
def dataFormat(inData):
    outData = []
    lineLen = len(inData)
    for i in range(1, lineLen):
        outData.append(tuple(inData[i][1:]))
    return outData

# Create Graph
def data2Graph(inData):
    tmpGraph = nx.Graph()
    for i in range(len(inData)):
        for j in range(len(inData)):
            if i == j:
                pass
            tmpGraph.add_edge(i, j, weight=inData[i][j])
    return tmpGraph