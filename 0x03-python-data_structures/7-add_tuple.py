#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    total = []
    for i in range(0, 2):
        if len(tuple_b) > i:
            x = tuple_b[i]
        else:
            x = 0

        if len(tuple_a) > i:
            z = tuple_a[i]
        else:
            z = 0
        total.append(x + z)
    return tuple(total)
