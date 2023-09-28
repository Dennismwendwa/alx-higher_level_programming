#!/usr/bin/env bash
# script that returns size of the body of url

url="$1"

curl -sI "$url" | grep -i "Content-Length" | cut -d " " -f 2
