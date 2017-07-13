import numpy as np
from sklearn.neighbors import KDTree
import csv

cached = False
cachedData = []
def dataParser():
    global cached
    global cachedData
    if cached:
        return cachedData
    data = []
    with open('dataset.csv', 'rb') as dataFile:
        reader = csv.reader(dataFile, delimiter=',')
        for row in reader:
            name = row[0]
            height = row[1]
            avgTemp = row[2]
            distZ = row[3]
            distX = row[4]
            tempArr = row[5:]
            data.append({"name": name,
                         "height": height,
                         "avgTemp": avgTemp,
                         "distZ": distZ,
                         "distX": distX,
                         "tempArr": np.array(tempArr).astype(np.float)})
    cachedData = data
    cached = True
    return data

treeConstructed = False
tree = object
def getMostSimilar(tarr):
    global treeConstructed
    global tree
    if not treeConstructed:
        data = dataParser()
        tempArrs = [element["tempArr"] for element in data]
        npArr = np.array(tempArrs)
        tree = KDTree(npArr, leaf_size=2)
        treeConstructed = True
    queryVal = tree.query(tarr, k=3)
    return queryVal
