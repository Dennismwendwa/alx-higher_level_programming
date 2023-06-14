#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    score = 0
    weight = 0

    for s, w in my_list:
        score += s * w
        weight += w

    return score / weight
