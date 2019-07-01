import random
import csv
import numpy

def randGen(maxRange):
    return (random.randint(0, maxRange))

def mapGenerator(citiesNumber, maxDistance):
    x = []
    y = []
    for i in range(citiesNumber):
        x.append(randGen(maxDistance))
        y.append(randGen(maxDistance))
    print(x, "\n", y)
    f = open("map.csv", 'w')
    for i, j in zip(x, y):
        f.write(str(i) + "," + str(j) + "\n")
    f.close()

def readMap(filename):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        x = []
        y = []
        for row in readCSV:
            xRow = row[0]
            yRow = row[1]

            x.append(int(xRow))
            y.append(int(yRow))

        print(x, "\n", y)


#mapGenerator(1000, 1000)
readMap("map.csv")
