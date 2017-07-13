import numpy as np
import sklearn as sk
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

import Queue
def getMostSimilar(target):
    nearestNeighbors = Queue.PriorityQueue()
    data = dataParser()
    bestScore = float("inf")
    mostSimilar = ""
    for row in data:

        score = bruteForceSearch(row["tempArr"], target)
        name = row["name"]
        e = Entry(score, name)
        nearestNeighbors.put(e)
        if(score < bestScore):
            bestScore = score
            mostSimilar = row["name"]
    k = 3
    mostSimilars = []
    for i in range(k):
        mostSimilars.append(nearestNeighbors.get().value)
    return mostSimilars


class Entry:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __cmp__(self, other):
         return cmp(self.priority, other.priority)

def bruteForceSearch(source, target):
    # takes in a source image array and a target image array and returns a value based on their abs difference
    diff = target - source
    diff = np.absolute(diff)
    return np.sum(diff)