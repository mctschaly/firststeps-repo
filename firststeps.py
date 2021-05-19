# -*- coding: utf-8 -*-

import sys

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Griaß di, {}".format(who_to_greet)
    return greeting


lago = "doof"


print(greet("Welt"))
print(greet("tschaly"))

print("Lago is {}!".format(lago))
print("script name is " + sys.argv[0])
