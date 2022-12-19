#!/usr/bin/python3
for num in range(0, 100):
    print("{}{}".format(num // 10, num % 10), end="")
    if num != 99:
        print("{}".format(", "), end="")
