#!/usr/bin/env bash
# script that send JSON POSt

url="$1"
file="$2"

curl -s "$url" -d "@$file" -X "Content-Type: application/json"
