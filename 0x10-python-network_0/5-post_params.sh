#!/usr/bin/env bash
# script that sends POST request

url="$1"
curl -sX "POST" "$url" -d "email=test@gmail.com&subject=I will always be here for PLD"
