#!/bin/bash
# display status code ofthe response
curl -sw '%{http_code}' "$1" -o /dev/null
