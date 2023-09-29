#!/usr/bin/python3
"""This script fetches url supplied"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
        decode_content = content.decode("utf-8")

    print("Body response:")
    print("    - type:", type(content))
    print("    - content:", content)
    print("    - utf8 content:", decode_content)

except Exception as e:
    pass
