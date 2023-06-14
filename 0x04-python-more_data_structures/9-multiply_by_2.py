#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = {}
    for ky, val in a_dictionary.items():
        new[ky] = val * 2
    return new
