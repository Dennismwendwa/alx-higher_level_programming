#!/bin/bash
# script that send JSON POSt
curl -s "$1" -d "@$2" -X "Content-Type: application/json"
