import data_loader

def debug(debugData):
    import pprint
    pprint.pprint(debugData)

dataPath = './data/test_data.csv'
poleData = data_loader.csv2Tuple(dataPath)
poleCoor = data_loader