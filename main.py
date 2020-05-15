#####################################
#  Author: Bi0x                     #
#  Github: bi0x@foxmail.com         #
#####################################

import data_loader, data_drawer
import networkx
import ant

def debug(debugData):
    import pprint
    pprint.pprint(debugData)

csvPath = './data/test_data.csv'
pointData = data_loader.dataFormat(data_loader.csv2Tuple(csvPath))
graphData = data_loader.data2Graph(pointData)
