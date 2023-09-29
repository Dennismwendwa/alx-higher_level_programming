#!/usr/bin/python3
"""This script fetches url supplied"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
        decode_content = content.decode("utf-8")

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(decode_content))

except Exception as e:
    pass
