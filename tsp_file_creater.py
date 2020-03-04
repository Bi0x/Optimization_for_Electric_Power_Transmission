#! -*- coding:utf-8 -*-
#####################################
#  Author: Biox                     #
#  Github: ytx2240067446@gmail.com  #
#####################################

# TSP 问题名
tspName = "Optimization_for_electric_power_transmission"
# TSP 问题类型 非对称旅行商问题 (其实应该是 MATSP 的)
tspType = "ATSP"
# TSP 问题描述
tspComment = "72 telegraph pole in LanZhi, Distance between both pole is asymmetric."
# 存在的点数
tspDimension = "29"


tspFile = open('./data/tspData.tsp', 'w')
tspFile.write("NAME: " + tspName + "\n")
tspFile.write("TYPE: " + tspType + "\n") 
tspFile.write("COMMENT: " )
tspFile.close()