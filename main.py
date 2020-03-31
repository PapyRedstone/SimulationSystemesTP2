#!/usr/bin/python3

from Random import *
import turtle
import numpy
import random

r = Random(517 ,0 ,8999)
scale = 10

def reset(x,y):
    root = turtle.getscreen()._root
    turtle.clear()
    root.withdraw()
    root.quit()

def draw(x, y):
    reset(None, None)
    root = turtle.getscreen()._root
    root.state('normal')
    turtle.speed(0)
    turtle.goto(x[0]*scale, y[0]*scale)
    turtle.pendown()

    for i in range(1, len(x)):
        turtle.goto(x[i]*scale, y[i]*scale)

    turtle.penup()
    turtle.onscreenclick(reset)

def drawUnique(posList):
    reset(None, None)
    root = turtle.getscreen()._root
    root.state('normal')
    turtle.speed(0)

    turtle.goto(posList[0][0]*scale, posList[0][0]*scale)
    turtle.pendown()

    for i in range(1, len(posList)):
        turtle.goto(posList[i][0]*scale, posList[i][1]*scale)

    turtle.penup()
    turtle.onscreenclick(reset)

def classique():
    print("\nNombre de pas de la simulation ?")
    nSteps = int(input())

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

    draw(x, y)

def getDirection():
    return r.random()%4
            
def sansRetour():
    print("\nNombre de pas de la simulation ?")
    nSteps = int(input())

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

    draw(x, y)

def passageUnique():
    print("\nNombre de pas de la simulation ?")
    nSteps = int(input())
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
        
        #print((x[i], y[i]))
        positions.append((x[i], y[i]))

    #print(positions)
    drawUnique(positions)

def verifyPosition(nextPos, positions):
    for position in positions:
        if nextPos == position:
            return False
    
    return True

def main():
    # congruance lineaire multiplicatif => c=0
    # a = 166
    # m = 49 999 is prime
    # r = Random(517 ,0 ,8999)
    #r.setSeed(5)
    r.testKhi2()

    functions = {
        "c":classique,
        "s":sansRetour,
        "u":passageUnique,
        "q":exit
    }

    while True:
        print("\n\n/!\ --- Pour fermer la fenetre de simulation, cliquer au milieu  à la fin (ne pas fermer via la croix)")
        print("\nType de marche aléatoire ?")
        print("\tClassique (c)")
        print("\tSans-retour (s)")
        print("\tPassage unique (u)")
        print("\tQuitter (q)")
        
        choice = input()
        #choice = "5" #for testing

        try:
            functions[choice]()
        except KeyError:
            print("Veuillez choisir une entree correcte")
        

if __name__ == "__main__":
    main()
