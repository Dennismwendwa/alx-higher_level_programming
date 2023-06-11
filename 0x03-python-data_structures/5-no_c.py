#!/usr/bin/python3

def no_c(my_string):
    my_str = list(my_string)
    [my_str.remove(n) for n in my_str if n == "c" or n == "C"]

    my_string = "".join(my_str)
    return my_string
