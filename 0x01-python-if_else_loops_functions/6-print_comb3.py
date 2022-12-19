#!/usr/bin/python3
for c in range(0, 10):
    for d in range(1, 10):
        if c < d and c != d:
            if c == 8 and d == 9:
                print("{}{}".format(c, d))
            else:
                print("{}{}".format(c, d), end=", ")
