import importDataset
import numpy as np
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline
from sklearn import linear_model, datasets, metrics

classifierConstructed = False
classifier = object
rbm = object
logistic = object
def getMostSimilar(tarr):
    global classifierConstructed
    global classifier
    global logistic
    global rbm
    data = importDataset.dataParser()
    if not classifierConstructed:
        tempArrs = [element["tempArr"] for element in data]
        npArr = np.array(tempArrs, 'float32')
        divider = lambda x: x / (255 * 5)
        adjustedArr = np.array([[divider(cell) for cell in element] for element in npArr])
        rbm = BernoulliRBM(n_components=100, random_state=0, batch_size=100, learning_rate=0.006, n_iter=10, verbose=True)
        logistic = linear_model.LogisticRegression()
        logistic.C = 1.0
        classifier = Pipeline(steps=[('rbm', rbm), ('logistic', logistic)])
        classifier.fit(adjustedArr, np.array([(1 if 'Human' in item["name"] else 0) for item in data], 'float32'))
        classifierConstructed = True
    prediction = classifier.predict([tarr])
    return "Human" if prediction == 1 else "Not Human"