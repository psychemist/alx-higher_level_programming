#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10
str = "Last digit of"

if mod > 5:
    print("{} {} is {} and is greater than 5".format(str, number, mod))
elif mod < 6 and mod != 0:
    print("{} {} is {} and is less than 6 and not 0".format(str, number, mod))
else:
    print("{} {} is {} and is 0".format(str, number, mod))
