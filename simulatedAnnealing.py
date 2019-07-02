import math as math
import matplotlib.pyplot as plt
import scipy as sy
import time as time
import numpy as np

'''
Class that contains datas from a city
'''
class City:
        def __init__(self, x=0, y=0, name="null"):
                self.x = x
                self.y = y
                self.name = name

'''
Method calculating the probability to keep the new solution
'''
def Acceptance (deltaE, Temp):
    proba = math.exp(-(deltaE/Temp))
    random = np.random.uniform
    if random < proba:
        return True
    else:
        return False


beginningTime = time.process_time()

# +++++++++++++++++++++
# Variables

N_trucks = 2
N_cities = 15
Temp = 20
TempMin = 5
Energie = 0
Coeff = 0.99

cities = []
x = [10, 83, 64, 44, 8, 34, 86, 12, 70, 87, 52, 24, 29, 66, 40]
y = [34, 90, 43, 72, 71, 28, 20, 10, 70, 54, 90, 93, 48, 16, 10]

for i in range(len(x)):
    cities.append(City(x[i], y[i]))

clusters = np.array_split(cities, N_trucks)
i = 0
for cluster in clusters:
    i += 1
    print("\n" + str(i))
    for city in cluster:
        print(str(city.x) + ", " + str(city.y))

while (Temp > TempMin):
        # Cluster selection (random)
        iCluster = np.random.randint(high=len(clusters))
        if len(clusters[iCluster]) == 0:
                continue
        
        # Index selection (in cluster)
        indexCity = np.random.randint(high=len(cluster))

endTime = time.process_time()
totalTime = endTime - beginningTime

print("\nBeginning Time: " + str(beginningTime))
print("End Time:       " + str(endTime))
print("Total Time:     " + str(totalTime))