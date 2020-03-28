#! -*- coding:utf-8 -*-
#####################################
#  Author: Biox                     #
#  Github: ytx2240067446@gmail.com  #
#####################################

import data_loader, data_drawer
import tsplib95
import networkx

def debug(debugData):
    import pprint
    pprint.pprint(debugData)

csvPath = './data/test_data.csv'
tspName = 'Lanzhi_5803'
data_loader.tspFileCreator(csvPath, tspName)
tspProblem = tsplib95.load_problem('./data/tsp_data.tsp')
graph = tspProblem.get_graph()
