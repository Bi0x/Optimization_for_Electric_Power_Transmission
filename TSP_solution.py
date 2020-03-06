#! -*- coding:utf-8 -*-

class TSPSolution:
    def __init__(self, rho, q, top):
        super().__init__()
        self.rho = rho                  # 信息素挥发因子
        self.q = q                      # 信息素浓度

    def solveStep(self, graph, colony, sales, start, limit, opt):
        size = len(graph.nodes)
        antColony = colony.colonyInit(size)
    
    def solveTSP(self, graph, colony, sales, start, gen_size, limit, opt):
        res = -1
    
    