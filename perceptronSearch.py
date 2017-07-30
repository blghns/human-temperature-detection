import numpy as np
from sklearn.linear_model import perceptron
import importDataset

net = object
netConstructed = False


def getMostSimilar(tarr):
    global net
    global netConstructed
    data = importDataset.dataParser()

    if not netConstructed:
        tempArrs = [element["tempArr"] for element in data]
        targetArrs = [element["name"] for element in data]
        npTempArrs = np.array(tempArrs)
        npTargetArrs = np.array(targetArrs)
        net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
        net.fit(npTempArrs, npTargetArrs)
        netConstructed = True
    pred = net.predict([tarr])
    return pred
