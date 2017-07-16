import csv
import numpy as np

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
