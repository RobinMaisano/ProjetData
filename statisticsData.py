from sklearn import linear_model

import matplotlib.pyplot as plt
import numpy as np
import csv
from statistics import median, mean, mode

def graph(X, Y, title):
    #----------------------------------------------------------------------------------------#
    # Step 1: training data

    maxX = max(X)
    maxY = max(Y)

    X = np.asarray(X)
    Y = np.asarray(Y)

    X = X[:,np.newaxis]
    Y = Y[:,np.newaxis]

    plt.scatter(X,Y)

    #----------------------------------------------------------------------------------------#
    # Step 2: define and train a model

    model = linear_model.LinearRegression()
    model.fit(X, Y)

    print(model.coef_, model.intercept_)
    logToFile("\nThe coefficient of the regression line is : ", str(model.coef_))
    logToFile("\nThe intersection point between the regression line and the y axis is : ", str(model.intercept_))
    #----------------------------------------------------------------------------------------#
    # Step 3: prediction

    x_new_min = 0.0
    x_new_max = (maxX + 0.2*maxX)

    X_NEW = np.linspace(x_new_min, x_new_max, 100)
    X_NEW = X_NEW[:,np.newaxis]

    Y_NEW = model.predict(X_NEW)

    plt.plot(X_NEW, Y_NEW, color='coral', linewidth=3)

    plt.grid()
    plt.xlim(x_new_min,x_new_max)
    plt.ylim(0,(maxY + 0.2*maxY))

    plt.title(title,fontsize=10)
    plt.xlabel('Number of cities')
    plt.ylabel('Time needed to resolve shortest path (in seconds)')

    plt.savefig("report/" + title + ".png", bbox_inches='tight')
#    plt.show()
    plt.close()

def openCSV(filename):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        citiesNumberList = []
        timeList = []
        truckNumberList = []
        for row in readCSV: #Read line by line
            firstRow = row[0]
            secondRow = row[1]
            thirdRow = row[2]

            citiesNumberList.append(float(firstRow)) #Put all the data in lists
            timeList.append(float(secondRow))
            truckNumberList.append((float(thirdRow)))

        print(citiesNumberList, "\n", timeList, "\n", truckNumberList)
        return citiesNumberList, timeList, truckNumberList

def dispatcheur(citiesNumberList, timeList, truckNumberList):

    #This method, generate statistics for all different number of truck used
    sortedTruckList = sorted(list(dict.fromkeys(truckNumberList))) #Sort list and remove duplicates
    print("sortedTruckList :", sortedTruckList)
    for truckNumber in sortedTruckList: # For all different number of truck used ...
        tempCitiesList = []
        tempTimeList = []
        tempTruckList = []
        for i in range(len(truckNumberList)): # Get the cities and the time needed ...
            if truckNumberList[i] == truckNumber:
                tempCitiesList.append(citiesNumberList[i])
                tempTimeList.append(timeList[i])
                tempTruckList.append(truckNumberList[i])
        title = str(truckNumber) + " Trucks"
        stats(tempCitiesList, tempTimeList, title) # ... And create stats


def stats (citiesNumberList, timeList, title):
    logToFile("Statistics with : ", title,"\n\n<h1 align=\"center\">","</h1>") # Write title to logfile
    reportFile.write("</h1>")
    logToFile("\ncitiesNumberList : ", str(citiesNumberList), "<br>")
    logToFile("\ntimeList : ", str(timeList), "<br>")
    logToFile("\nThe lists are composed of ", str(len(citiesNumberList)), "<br>")
    reportFile.write(" data <br>\n")

    graph(citiesNumberList, timeList, title) # Generate the scatter graph with the regression line
    medianTemp = median(timeList) # Calculate the Median
    meanTemp = mean(timeList) # Calculate the Mean
    rangeTemp = (max(timeList) - min(timeList)) # Calculate the range
    q1temp = np.percentile(np.asarray(timeList), 25) # Calculate the first quartile
    q3temp = np.percentile(np.asarray(timeList), 75) # Calculate the third quartile
    varianceTemp = np.var(np.asarray(timeList), 0) # Calculate the variance

    logToFile("\nThe median is : ", str(medianTemp), "<br>") # Log all the statistics
    logToFile("\nThe mean is : ", str(meanTemp), "<br>")
    logToFile("\nThe range is : ", str(rangeTemp), "<br>")
    logToFile("\nThe first quartile is : ", str(q1temp), "<br>")
    logToFile("\nThe third quartile is : ", str(q3temp), "<br>")
    logToFile("\nThe variance is : ", str(varianceTemp), "<br>")

    reportFile.write("\n<p align=\"center\">\n\t<IMG src=\"")
    reportFile.write(title)
    reportFile.write(".png\" alt=\"")
    reportFile.write(title)
    reportFile.write("\" border=\"0\" width=\"562\" height=\"452\">\n</p>")

def logToFile(string, value, firstHtmlTag = None, lastHtmlTag = None):
    if firstHtmlTag is not None:
        reportFile.write(firstHtmlTag)
    reportFile.write(string)
    reportFile.write(value)
    if lastHtmlTag is not None:
        reportFile.write(lastHtmlTag)

def initReportFile():
    reportFile.write("<!DOCTYPE html>\n<html>\n<head lang=\"en\">\n\t<meta charset=\"UTF-8\">\n"
                     "\t<title>Report of statistics</title>\n</head>\n<body>")
    reportFile.write("All the statistics have been done on the time needed to resolve the shortest path, "
                     "not on the number of cities <br>")

reportFile = open("report/report.html", "w")
initReportFile()
citiesNumberList, timeList, truckNumberList = openCSV('stats.csv')
stats(citiesNumberList,timeList,"Global stats")
dispatcheur(citiesNumberList, timeList, truckNumberList)
reportFile.close()