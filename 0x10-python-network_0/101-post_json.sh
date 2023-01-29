#!/bin/bash
# send a post request with a json file
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
