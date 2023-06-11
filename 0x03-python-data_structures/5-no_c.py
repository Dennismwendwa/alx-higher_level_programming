#!/usr/bin/python3

def no_c(my_string):
    my_str = list(my_string)
    for i in my_str:
        if i == "c" or i == "C":
            my_str.remove(i)
    my_str = "".join(my_str)
    return my_str
