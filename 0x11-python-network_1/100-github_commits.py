#!/usr/bin/python3
"""this script ptints the recent 10 commits from repo rails"""
import requests
from sys import argv


repo_name = argv[1]
owner = argv[2]

url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'

try:
    response = requests.get(url)
    response.raise_for_status()

    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get("sha")
        author_name = commit.get("commit", {}).get("author", {}).get("name")

        if sha and author_name:
            print("{}: {}".format(sha, author_name))

except requests.exceptions.RequestException as e:
    exit("Error: {}".format(e))
