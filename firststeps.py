# This Python file uses the following encoding: utf-8

import sys

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    lago = "doof"
    greeting = "Griaß di, {}".format(who_to_greet)
    return greeting


print(greet("Welt"))
print(greet("tschaly"))
