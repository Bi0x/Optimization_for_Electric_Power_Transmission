#! -*- coding:utf-8 -*-
#####################################
#  Author: Biox                     #
#  Github: ytx2240067446@gmail.com  #
#####################################

import data_loader, data_drawer

def debug(debugData):
    import pprint
    pprint.pprint(debugData)

dataPath = './data/test_data.csv'
poleData = data_loader.csv2Tuple(dataPath)
poleCoor = data_loader.dataFormat(poleData)
data_drawer.dataDrawer_All(poleCoor, 7)