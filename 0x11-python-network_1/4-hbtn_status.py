#!/usr/bin/python3
"""this script fetches for url using request module"""
import requests


url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()

    print("Body response:")
    print("    - type:", type(response.text))
    print("    - content:", response.text)

except requests.exceptions.RequestException as e:
    pass
