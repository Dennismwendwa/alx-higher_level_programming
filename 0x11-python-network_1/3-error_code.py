#!/usr/bin/python3
"""this script prints the status code of the response"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            response_b = response.read().decode("utf-8")
            print(response_b)

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
