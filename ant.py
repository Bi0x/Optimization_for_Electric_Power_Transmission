
class antColony:
    def __init__(self, alpha, beta):
        super().__init__()
        self.alpha = alpha      # 信息素启发因子
        self.beta = beta        # 期望启发因子

    def colonyInit(self, size): # 蚁群初始化
        colony = []
        for i in range(size):
            colony.append(antSingle(self.alpha, self.beta))
        return colony


class antSingle:
    def __init__(self, alpha, beta):
        super().__init__()
        self.alpha = alpha      # 信息素启发因子
        self.beta = beta        # 期望启发因子

    