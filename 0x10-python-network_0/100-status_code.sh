#!/bin/bash
# script that display status code of response
curl -so /dev/null -w "%{htt_code}" "$1"
