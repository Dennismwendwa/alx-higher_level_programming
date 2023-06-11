#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        my_str = my_string.translate({ord(ch): None for ch in "Cc"})


    return my_str
