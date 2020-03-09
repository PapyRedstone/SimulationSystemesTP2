#!/usr/bin/python3

from Random import *

def main():
    r = Random(50,10,60)
    r.setSeed(5)
    for _ in range(5):
        print(r.random())

if __name__ == "__main__":
    main()
