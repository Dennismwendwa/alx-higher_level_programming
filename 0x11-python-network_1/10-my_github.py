#!/usr/bin/python3
"""this script sends request to github"""
import requests
from sys import argv


if __name__ == "__main__":

    username = argv[1]
    token = argv[2]

    url = "https://api.github.com/user"

    auth = (username, token)

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()

        user_data = response.json()
        user_id = user_data.get("id")

        if user_id is not None:
            print(user_id)
        else:
            print("None")

    except requests.exceptions.RequestException as e:
        print("None")
