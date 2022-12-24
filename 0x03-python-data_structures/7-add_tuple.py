#!/usr/bin/python3
def check_t(tuple_x):
    if len(tuple_x) < 2:
        if len(tuple_x) == 0:
            new_tuple = (0, 0)
        if len(tuple_x) == 1:
            new_tuple = (tuple_x[0], 0)
    elif len(tuple_x) > 2:
        new_tuple = tuple_x[:2]
    else:
        new_tuple = tuple_x
    return new_tuple


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check_t(tuple_a)
    tuple_b = check_t(tuple_b)
    sum_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return sum_tuple

'''  a = len(tuple_a)
    b = len(tuple_b)

    sums = ((tuple_a[0] if a > 0 else 0) + (tuple_b[0] if b > 0 else 0),
            (tuple_a[1] if a > 1 else 0) + (tuple_b[1] if b > 1 else 0))

    return sums
'''

# tuple_a += (0, 0)
# tuple_b += (0, 0)
# return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
