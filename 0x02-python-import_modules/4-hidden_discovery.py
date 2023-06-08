#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import hidden_4

obj = dir(hidden_4)
nams = list(obj)

for nam in nams:
    if nam[0] is not "_":
        print("{:s}".format(nam))
