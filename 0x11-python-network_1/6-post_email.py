#!/usr/bin/python3
"""this script prints data from the response"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = {"email": email}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print("Your email is:", response.text)

    except requests.exceptions.RequestException as e:
        pass
