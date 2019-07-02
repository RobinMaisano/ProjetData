import random
import csv

def randGen(maxRange):
    return (random.randint(0, maxRange))

def mapGenerator(citiesNumber, maxDistance, filename):
    x = []
    y = []
    for i in range(citiesNumber):
        x.append(randGen(maxDistance))
        y.append(randGen(maxDistance))
    print(x, "\n", y)
    f = open(filename, 'w')
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
        return x,y
'''
class City:
    def __init__(self, x=0, y=0, name="null"):
        self.x = x
        self.y = y
        self.name = name

def listToMatrix(x, y):
    matrixLength = len(x)
    print("Le longueur est : ", matrixLength, "\n\n")
    matrix = []
    citiesList = []
    for i in range(matrixLength-1):
        matrix.append([0] * matrixLength)
#        print(matrix[i])
    for j in range(len(x)):
#        print("\nx : ", x[j], "y : ", y[j])
        citiesList.append(City(x[j], y[j], j))
        print(citiesList[j].name)'''

mapGenerator(200, 500, "maps/map02.csv")
x, y = readMap("maps/map1.csv")
#listToMatrix(x, y)