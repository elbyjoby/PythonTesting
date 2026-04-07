# This is a sample Python script.
from unittest import result


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_weather(temp):
    if temp > 20:
        return "hot"
    else:
        return "cool"

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b