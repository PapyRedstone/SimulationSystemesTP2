from time import time

class Random:
    def __init__(self, a, c, m):
        self.a = a
        self.c = c
        self.m = m
        self.setSeed(time())
    
    def random(self):
        self.currentNumber = (self.a * self.currentNumber + self.c) % self.m
        return self.currentNumber

    def setSeed(self, s):
        self.seed = s % self.m
        self.currentNumber = s
