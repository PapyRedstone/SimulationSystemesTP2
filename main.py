#!/usr/bin/python3

from Random import *

def main():
    # congruance lineaire multiplicatif => c=0
    # a = 166
    # m = 49 999 is prime
    r = Random(517 ,0 ,8999)
    #r.setSeed(5)
    r.testKhi2()

if __name__ == "__main__":
    main()
