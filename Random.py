from time import time

class Random:
    def __init__(self, a, c, m):
        self.a = a
        self.c = c
        self.m = m
        self.setSeed(round(time()))
    
    def random(self):
        self.currentNumber = (self.a * self.currentNumber + self.c) % self.m
        return self.currentNumber

    def setSeed(self, s):
        self.seed = s % self.m
        self.currentNumber = s

    def testKhi2(self):
        n = 100000 #nombre de tirages
        
        data = {
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0,
            10:0,
            11:0,
            12:0
        }

        for _ in range(n):
            # on tire deux des aleatoirement
            dice = (self.random()%6)+1 + (self.random()%6)+1
            data[dice] += 1

        #on regroupe des categories
        data[3] += data.pop(2)
        data[11] += data.pop(12)

        print(data)

        #le nombre de d'occurences par categories theoriques
        expectedNumber = {
            3:n/36 + n/18,
            4:n/12,
            5:n/9,
            6:n*5/36,
            7:n/6,
            8:n*5/36,
            9:n/9,
            10:n/12,
            11:n/36 + n/18
        }

        print(expectedNumber)

        #on verifie que le theorique et empiriques on le meme jeu de donnees
        if data.keys() != expectedNumber.keys():
            print("ERROR: Data and expected data sould have the same keys")
            return

        #on calcule C, qui appartient est un VA de Khi2 a 8 degre de liberte
        C=0
        for i in data.keys():
            C += (data[i] - expectedNumber[i])**2 / expectedNumber[i]

        print("C = {}".format(C))

        khi2Table = {
            "10%"  : 13.36,
            "5%"   : 15.51,
            "2.5%" : 17.53,
            "1%"   : 20.09,
            "0.5%" : 21.96
        }

        #On accepet ou rejete H0 en fonction de la table de Khi2 et de la valeur C calcule
        accepted = False
        for k,v in khi2Table.items():
            if C < v:
                accepted = True
                print("H0 accepte a {} (valeur = {})".format(k,v))
                break

        if not accepted:
            print("H0 rejeter a 0.5%")
        

        

