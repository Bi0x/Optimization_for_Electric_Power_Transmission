#! -*- coding:utf-8 -*-

import networkx as netx 
import matplotlib.pyplot as plt 
import numpy as np 

# Draw Data
def dataDrawer_All(inData, lenData):
    dataGraph = netx.Graph()
    dataMatrix = np.array(inData)
    for i in range(lenData):
        for j in range(lenData):
            if i == j:
                continue
            dataGraph.add_edge(i, j, weight = dataMatrix[i][j])
    pos = netx.spring_layout(dataGraph, iterations=20)
    netx.draw(dataGraph, pos, with_labels = True, node_size = 30)
    plt.show()