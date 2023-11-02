#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':
    switcher = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div,
    }
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        for (operator, func) in switcher.items():
            if operator == argv[2]:
                print("{} {} {} = {}".format(a, operator, b, func(a, b)))
                exit(0)
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
