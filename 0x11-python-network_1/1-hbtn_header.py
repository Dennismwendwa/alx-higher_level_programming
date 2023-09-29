#!/usr/bin/python3
"""this script display the value of X-Request-id from response"""
import urllib.request
from sys import argv


url = argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.info().get("X-Request-Id")
        if x_request_id is not None:
            print(x_request_id)

except Exception as e:
    pass
