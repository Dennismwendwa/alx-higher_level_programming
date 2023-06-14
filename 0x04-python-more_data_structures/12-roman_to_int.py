#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    reslt = 0
    prev_value = 0

    for x in roman_string[::-1]:
        val = roman_values.get(x, 0)

        if val < prev_value:
            reslt -= val
        else:
            reslt += val

        prev_value = val

    return reslt
