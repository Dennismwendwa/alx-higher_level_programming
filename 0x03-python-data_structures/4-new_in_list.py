#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    cp_ls = my_list.copy()
    length = len(cp_ls) - 1
    if idx > length or idx < 0:
        return cp_ls
    cp_ls[idx] = element
    return cp_ls
