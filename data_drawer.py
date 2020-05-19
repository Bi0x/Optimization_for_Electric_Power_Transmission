import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np 

# Draw Data
def drawAll(inData, lenData):
    dataGraph = nx.Graph()
    dataMatrix = np.array(inData)
    for i in range(lenData):
        for j in range(lenData):
            if i == j:
                continue
            dataGraph.add_edge(i, j, weight = dataMatrix[i][j])
    pos = nx.spring_layout(dataGraph, iterations=20)
    nx.draw(dataGraph, pos, with_labels = True, node_size = 30)
    plt.show()
