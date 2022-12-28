#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    idx = 0
    for idx in range(list_length):
        result = 0
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            my_list_3 += [result]
    return my_list_3
