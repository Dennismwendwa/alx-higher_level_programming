#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str
    lst = list(str)
    for h in range(0, len(str) - 1):
        if h > n:
            lst[h] = lst[h + 1]
        new = "".join(lst)
        return new[:-1]
