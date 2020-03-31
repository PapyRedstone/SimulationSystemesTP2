#!/usr/bin/python3

from Random import *
import numpy
import random
import statistics
import matplotlib.pyplot as plt

r = Random(517 ,0 ,8999)
scale = 10

def getDirection():
    return r.random()%4

def distance(endPoint):
    return (endPoint[0] - 0)**2 + (endPoint[1] - 0)**2 

def classique(nSteps):

    x = numpy.zeros(nSteps)
    y = numpy.zeros(nSteps)
    
    for i in range(1, nSteps): 
        val = getDirection()
        if val == 0: #droite
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif val == 1: #gauche
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif val == 2: #haut
            x[i] = x[i - 1] 
            y[i] = y[i - 1] + 1
        else: #bas
            x[i] = x[i - 1] 
            y[i] = y[i - 1] - 1

    return distance((x[-1],y[-1]))

            
def sansRetour(nSteps):
    x = numpy.zeros(nSteps)
    y = numpy.zeros(nSteps)
    previous = None
    
    for i in range(1, nSteps):
        val = getDirection()

        while True:
            if val == 0 and previous == 1: #going right from a left
                val = getDirection()
            elif val == 1 and previous == 0: #going left from a right
                val = getDirection()
            elif val == 2 and previous == 3: #going up from a down
                val = getDirection()
            elif val == 3 and previous == 2: #going down from a up
                val = getDirection()
            else:
                break

        previous = val

        if val == 0: #droite
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif val == 1: #gauche
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif val == 2: #haut
            x[i] = x[i - 1] 
            y[i] = y[i - 1] + 1
        elif val == 3: #bas
            x[i] = x[i - 1] 
            y[i] = y[i - 1] - 1

    return distance((x[-1],y[-1]))

def passageUnique(nSteps):
    counter = 0
    positions = []

    x = numpy.zeros(nSteps)
    y = numpy.zeros(nSteps)

    positions.append((0, 0))

    for i in range(1, nSteps):

        if counter >= nSteps:
                break

        while True:
            if counter >= nSteps:
                break

            val = getDirection()

            if val == 0: #droite
                x[i] = x[i - 1] + 1
                y[i] = y[i - 1]
            elif val == 1: #gauche
                x[i] = x[i - 1] - 1
                y[i] = y[i - 1]
            elif val == 2: #haut
                x[i] = x[i - 1] 
                y[i] = y[i - 1] + 1
            elif val == 3: #bas
                x[i] = x[i - 1] 
                y[i] = y[i - 1] - 1

            nextPos = (x[i], y[i])
            counter += 1

            if verifyPosition(nextPos, positions):
                break
        
        positions.append((x[i], y[i]))

    return distance(positions[-1])

def verifyPosition(nextPos, positions):
    for position in positions:
        if nextPos == position:
            return False
    
    return True

def main():
    classicRW = {}
    sRRW = {}
    pURW = {}

    nSteps = int(input("Nombre de pas maximal : "))
    nSimu = int(input("Nombre de simulations par pas : "))

    for i in range(1, nSteps+1):
        classic = []
        sR = []
        pU = []
        for j in range(0, nSimu):
            classic.append(classique(i))
            sR.append(sansRetour(i))
            pU.append(passageUnique(i))
            #print(classic)
        
        classicRW[i-1] = statistics.mean(classic) 
        sRRW[i-1] = statistics.mean(sR) 
        pURW[i-1] = statistics.mean(pU) 

    data1 = {"x":[], "y":[]}
    data2 = {"x":[], "y":[]}
    data3 = {"x":[], "y":[]}
    
    for n, meanSquare in classicRW.items():
        data1["x"].append(n)
        data1["y"].append(meanSquare)

    for n, meanSquare in sRRW.items():
        data2["x"].append(n)
        data2["y"].append(meanSquare)

    for n, meanSquare in pURW.items():
        data3["x"].append(n)
        data3["y"].append(meanSquare)

    plt.plot(data1["x"], data1["y"], label = "Random walks")
    plt.plot(data2["x"], data2["y"], label = "Nonreversing walks")
    plt.plot(data3["x"], data3["y"], label = "Self avoiding walks")

    plt.xlabel('Number of steps')
    plt.ylabel('Mean squared end-to-end displacement')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
