import numpy as np
from sklearn.neighbors import KDTree
import importDataset

treeConstructed = False
tree = object
def getMostSimilar(tarr):
    global treeConstructed
    global tree
    data = importDataset.dataParser()
    if not treeConstructed:
        tempArrs = [element["tempArr"] for element in data]
        npArr = np.array(tempArrs)
        tree = KDTree(npArr, leaf_size=2)
        treeConstructed = True
    closenessValues, indices = tree.query([tarr], k=3)
    names = [data[index]["name"] for index in indices.tolist()[0]]
    return names
