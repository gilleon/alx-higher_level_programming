#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lent1 = len(tuple_a)
    lent2 = len(tuple_b)

    if (lent1 >= 2 and lent2 >= 2):
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    elif (lent1 == 1 and lent2 == 1):
        return (tuple_a[0] + tuple_b[0], 0)
    elif (lent1 == 0 and lent2 == 0):
        return (0, 0)
    elif (lent1 == 1 and lent2 >= 2):
        return (tuple_a[0] + tuple_b[0], tuple_b[1])
    elif (lent1 == 0 and lent2 >= 2):
        return (tuple_b[0], tuple_b[1])
    elif (lent1 >= 2 and lent2 == 1):
        return (tuple_a[0] + tuple_b[0], tuple_a[1])
    elif (lent1 >= 2 and lent2 == 0):
        return (tuple_a[0], tuple_a[1])
    elif (lent1 == 1 and lent2 == 0):
        return (tuple_a[0], 0)
    elif (lent1 == 0 and lent2 == 1):
        return (tuple_b[0], 0)
