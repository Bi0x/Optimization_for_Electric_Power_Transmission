#! -*- coding:utf-8 -*-

class TSPSolution:
    def __init__(self, rho, q, top):
        super().__init__()
        self.rho = rho                  # 信息素挥发因子
        self.q = q                      # 信息素浓度

    # 边信息素值初始化
    def initPheromone(graph):
        for i, j in graph.edges:
            w = graph.edges[i, j]['weight']
            if w == 0:
                w = 1e99
            graph.edges[i, j].setdefault('pheromone', 1 / w)

    def findSolution(self, graph, colony, sales, startPole, iterTimes, opt):
        size = len(graph.nodes)
        antColony = colony.colonyInit(size)
        for i in range()

    
    def findBest(self, graph, colony, sales, start, gen_size, limit, opt):
        res = -1
        initPheromone(graph)
