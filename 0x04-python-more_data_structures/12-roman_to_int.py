#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0
    arab_num = 0
    for i in range(len(roman_string)):
        if roman_string[i] == 'M':
            if i and roman_string[i-1] == 'C':
                arab_num -= 200
            arab_num += 1000
        if roman_string[i] == 'D':
            if i and roman_string[i-1] == 'C':
                arab_num -= 200
            arab_num += 500
        if roman_string[i] == 'C':
            if i and roman_string[i-1] == 'X':
                arab_num -= 20
            arab_num += 100
        if roman_string[i] == 'L':
            if i and roman_string[i-1] == 'X':
                arab_num -= 20
            arab_num += 50
        if roman_string[i] == 'X':
            if i and roman_string[i-1] == 'I':
                arab_num -= 2
            arab_num += 10
        if roman_string[i] == 'V':
            if i and roman_string[i-1] == 'I':
                arab_num -= 2
            arab_num += 5
        if roman_string[i] == 'I':
            arab_num += 1
    return arab_num
