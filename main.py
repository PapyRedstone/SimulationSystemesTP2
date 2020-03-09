#!/usr/bin/python3

from Random import *

def main():
    r = Random(591,149,600)
    #r.setSeed(5)
    for _ in range(5):
        print(r.random())

if __name__ == "__main__":
    main()
