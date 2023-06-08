#!/usr/bin/python3

if __name__ == "__main__":
    import sys

sum = 0
index = 1

while index < len(sys.argv):
    sum += int(sys.argv[index])
    index += 1

print("{:d}".format(sum))
