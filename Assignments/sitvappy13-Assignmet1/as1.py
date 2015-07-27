#!/usr/bin/python3

import sys


Zero = ["  000  ",
        " 0   0 ",
        "0     0",
        "0     0",
        "0     0",
        " 0   0 ",
        "  000  "]
One = [" 1 ",
       "11 ", 
       " 1 ", 
       " 1 ", 
       " 1 ", 
       " 1 ", 
       "111"]
Two = [" 222 ", "2   2", "2  2 ", "  2  ", " 2   ", "2    ", "22222"]
Three = [" 333 ", "3   3", "    3", "  33 ", "    3", "3   3", " 333 "]
Four = ["   4  ", "  44  ", " 4 4  ", "4  4  ", "444444", "   4  ",
        "   *  "]
Five = ["55555", "5    ", "5    ", " 555 ", "    5", "5   5", " 555 "]
Six = [" 666 ", "6    ", "6    ", "6666 ", "6   6", "6   6", " 666 "]
Seven = ["77777", "     7", "    7 ", "   7  ", "  7   ", " 7    ", "7    "]
Eight = ["  888 ", "8   8", "8   8", " 888 ", "8   8", "8   8", "  888 "]
Nine = [" 9999", "9   9", "9   9", " 9999", "    9", "    9", "    9"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    numword = sys.argv[1]        
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(numword):
            number = int(numword[column])
#            print(number)
            digit = Digits[number]
            line += digit[row] + "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: 05printdigits.py <number>")
except ValueError as err:
    print(err, "in", numword)
