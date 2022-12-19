#!/usr/bin/python3
for alph in range(ord('a'), ord('z')+1):
    if alph != 101 and alph != 113:
        print("{}".format(chr(alph)), end="")
