#!/bin/bash
# script that display status code of response
curl -so /dev/null -w "%{http_code}" "$1"
