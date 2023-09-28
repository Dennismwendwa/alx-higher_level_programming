#!/bin/bash
# script that uses DELETE request

url="$1"
curl -sX DELETE "$url"
