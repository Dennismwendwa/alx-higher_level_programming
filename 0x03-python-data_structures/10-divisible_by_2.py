#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        nw_l = []
        for i in my_list:
            if i % 2 == 0:
                nw_l.append(True)

            else:
                nw_l.append(False)
        return nw_l
