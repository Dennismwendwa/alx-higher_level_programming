#!/usr/bin/python3
"""This script reads stdin line by line"""


import sys


total_file_size = 0
status_counts = {}

try:
    for j, line in enumerate(sys.stdin, 1):
        try:
            parts = line.split()
            ip = parts[0]
            status_code = parts[8]
            file_size = parts[10]

            total_file_size += int(file_size)

            if status_code in status_counts:
                ststus_counts[status_code] += 1
            else:
                status_counts[status_code] = 1

            if j % 10 == 0:
                print(f"File size: {total_file_size}")
                for code, count in sorted(status_counts.items()):
                    print(f"{code}: {count}")
                print()

        except (IndexError, ValueError):
                pass

except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")
