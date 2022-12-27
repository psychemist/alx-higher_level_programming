#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    arab_num = 0
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, x in zip(roman_string, roman_string[1:]):
        if i not in nums.keys():
            return 0
        elif nums[i] >= nums[x]:
            arab_num += nums[i]
        else:
            arab_num -= nums[i]
    arab_num += nums[roman_string[-1]]
    return arab_num
