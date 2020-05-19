#####################################
#  Author: Bi0x                     #
#  Github: bi0x@foxmail.com         #
#####################################

import data_loader, data_drawer
import tsplib95
import networkx
import ant

def debug(debugData):
    import pprint
    pprint.pprint(debugData)

tspProblem = tsplib95.load('./data/lanzhi.tsp')

'''
csvPath = './data/test_data.csv'
pointData = data_loader.dataFormat(data_loader.csv2Tuple(csvPath))
graphData = data_loader.data2Graph(pointData)
'''