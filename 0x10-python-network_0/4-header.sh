#!/url/bin/env bash
# script that prints body of the responce

url="$1"
curl -s "$url" -H "X-School-User-Id: 98"
