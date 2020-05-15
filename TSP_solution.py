
import networkx as nx

class TSPSolution:
    def __init__(self, rho, q, top):
        super().__init__()
        self.rho = rho                  # 信息素挥发因子
        self.q = q                      # 信息素浓度

    # 边信息素值初始化
    def initPheromone(self, graph):
        for i, j in graph.edges:
            graph.edges[i, j].setdefault('pheromone', 1 / graph.edges[i, j]['weight'])

    def findSolution(self, graph, colony, sales, startPole, iterTimes, opt):
        size = len(graph.nodes)
        ants = colony.colonyInit(size)
        for i in range()

    def findBest(self, graph, colony, sales, start, gen_size, limit, opt):
        res = -1
        initPheromone(graph)

