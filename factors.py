#!/usr/bin/python3

from sys import argv
def print_factor(number):
    i = 2
    num = number
    while True:
        if num % i == 0:
            print("{:d}={:d}*{:d}".format(number, num // i, i))
            return
        i += 1

with open(argv[1], "r") as lfile:
    for i in lfile.read().strip().split("\n"):
        print_factor(int(i))
