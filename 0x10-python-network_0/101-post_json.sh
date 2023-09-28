#!/bin/bash
# script that send JSON POSt
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
