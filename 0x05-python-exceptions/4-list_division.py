#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    idx = 0
#    for num1, num2 in zip(my_list_1, my_list_2):
    for idx in range(list_length):
        try:
#            result = num1 / num2
            result = my_list_1[idx] / my_list_2[idx]
        except IndexError:
            print("out of range")
            result = 0 
        except TypeError:
            print("wrong type")
            result = 0 
        except ZeroDivisionError:
            print("division by 0")
            result = 0 
        finally:
            my_list_3 += [result]
    return my_list_3
