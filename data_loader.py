
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

def tspFileCreator(csvPath, tspName):
    tspFile = open('./data/tsp_data.tsp', 'w')
    poleData = csv2Tuple(csvPath)
    poleCoor = dataFormat(poleData)
    tspProblem = 'NAME: ' + tspName + '\n'
    tspProblem += 'TYPE: TSP\n'
    tspProblem += 'COMMENT: ' + tspName + ' TSP Problem\n'
    tspProblem += 'DIMENSION: ' + str(len(poleCoor[0])) + '\n'
    tspProblem += 'EDGE_WEIGHT_TYPE: EXPLICIT\n'
    tspProblem += 'EDGE_WEIGHT_FORMAT: FULL_MATRIX\nDISPLAY_DATA_TYPE: NO_DISPLAY\n'
    tspProblem += 'EDGE_WEIGHT_SECTION\n'
    for i in range(len(poleCoor)):
        for j in poleCoor[i]:
            tspProblem += str(j) + ' '
        tspProblem += '\n'
    tspProblem += "EOF\n"
    tspFile.write(tspProblem)
    tspFile.close()
