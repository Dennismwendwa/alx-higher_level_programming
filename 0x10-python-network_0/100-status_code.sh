#!/usr/bin/env bash
# script that display status code of response

url="$1"
curl -so /dev/null -w "%{htt_code}" "$url"
