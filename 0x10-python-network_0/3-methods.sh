#!/usr/bin/env bash
# script that display methods allowed

url="$1"
curl -sI "$url" | grep "Allow" | cut -d " " -f 2-
