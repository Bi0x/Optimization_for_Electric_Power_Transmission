#! -*- coding:utf-8 -*-

class TSPSolution:
    def __init__(self, rho, q, top):
        super().__init__()
        self.rho = rho                  # 信息素挥发因子
        self.q = q                      # 信息素浓度

    def initPheromone(graph)

    def findSolution(self, graph, colony, sales, start, limit, opt):
        size = len(graph.nodes)
        antColony = colony.colonyInit(size)

        for i, j in graph.edges:
            w = graph.edges[i, j]['weight']
            if w == 0:

    
    def findBest(self, graph, colony, sales, start, gen_size, limit, opt):
        res = -1
        for i in 