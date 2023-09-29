#!/usr/bin/python3
"""this script sends post request to url"""
import requests
from sys import argv


if len(argv) == 2:
    q = argv[1]
else:
    q = ""

url = "http://0.0.0.0:5000/search_user"
data = {"q": q}

try:
    response = requests.post(url, data=data)
    response.raise_for_ststus()

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data["id"], json_data["name"]))
        else:
            print("No result")
    except ValueError:
        pass
except requests.exceptions.RequestException as e:
    print("{}".format(e))