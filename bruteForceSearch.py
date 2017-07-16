import numpy as np
import importDataset


import Queue
def getMostSimilar(target):
    nearestNeighbors = Queue.PriorityQueue()
    data = importDataset.dataParser()
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