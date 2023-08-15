#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics"""


import sys


if __name__ == "__main__":
    siz = [0]
    code = ['200', '300', '400', '401', '403', '404', '405', '500']

    def look_match(line):
        try:
            line = line[:-1]
            ele = line.split(' ')
            siz[0] += int(ele[-1])
            cody = int(ele[-2])
            if cody in code:
                code[cody] += 1
        except Exception as e:
            pass

    def print_stat():
        print("File size: {}".format(siz[0]))
        for m in sorted(code.keys()):
            if code[m]:
                print("{}: {}".format(m, code[m]))
    m = 1
    try:
        for line in sys.stdin:
            look_match(line)
            if m % 10 == 0:
                print_stat()
            m += 1
    except KeyboardInterrupt:
        print_stat()
        raise
    print_stat()
