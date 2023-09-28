#!/bin/bash
# script that returns size of the body of url
curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f 2
