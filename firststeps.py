# -*- coding: utf-8 -*-

from decimal import Decimal
from fractions import Fraction
import sys
import math

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Griaß di, {}".format(who_to_greet)
    return greeting


lago = "doof"


print(greet("Welt"))
print(greet("tschaly"))

print("Lago is {}!".format(lago))
print("script name is '{}'".format(sys.argv[0]))


def fac(n):
    if n <= 1:
        return 1
    else:
        return fac(n - 1) * n


print("100! = {}".format(fac(100)))


def euler(n):
    e = Fraction(0)
    for i in range(n):
        e = e + Fraction(1, fac(i))

    return e


print("e after 10 iterations is {}".format(euler(10)))
print("e after 100 iterations is {}".format(euler(100)))
print(Decimal(math.acos(-1)))

print("type of 1 is {}".format(type(1)))
print("type of lago is {}".format(type(lago)))
print("type of fac is {}".format(type(fac)))


class Dog:
    def sound(self):
        print("bark")


d = Dog()
print(type(d))
d.sound()
