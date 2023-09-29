#!/usr/bin/python3
"""this script uses requests to print X-Request-Id"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get("X-Request-Id")

        if x_request_id:
            print(x_request_id)

    except requests.exceptions.RequestException as e:
        pass
