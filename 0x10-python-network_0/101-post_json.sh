#!/bin/bash
# send a post request with a json file
curl -s -H POST  "Content-Type: application/json" -d "@$2" "$1"
