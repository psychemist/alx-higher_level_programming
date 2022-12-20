#!/usr/bin/python3
def toUpper(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return chr(ord(c)-32)
    else:
        return c


def uppercase(str):
    for char in str:
        print("{}".format(toUpper(char)), end="")
    print("")
