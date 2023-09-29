#!/usr/bin/python3
"""this script sends a POST request"""
import urllib.request
import urllib.parse
from sys import argv


url = argv[1]
email = argv[2]

data = {"email": email}
data = urllib.parse.urlencode(data)
data = data.encode("utf-8")

try:
    with urllib.request.urlopen(url, data=data) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)

except Exception as e:
    pass
