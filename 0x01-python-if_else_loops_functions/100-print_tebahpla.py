#!/usr/bin/python3
def checkAl(c):
    if c % 2 == 0:
        return (chr(c + 32))
    else:
        return (chr(c))


for alph in range(90, 64, -1):
    print("{}".format(checkAl(alph)), end="")
