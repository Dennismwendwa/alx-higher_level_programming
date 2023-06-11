#!/usr/bin/python3
def element_at(my_list, idx):
    length = 0
    for _ in my_list:
        length += 1

    if idx > length or idx < 0:
        return None
    return my_list[idx]
