#!/usr/bin/env bash
# script that prints you got me from server responce

curl -sL -X -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
