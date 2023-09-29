#!/usr/bin/python3
"""this scripts response status code"""
import requests
from sys import argv


url = argv[1]

try:
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)

except requests.exceptions.RequestException as e:
    pass
