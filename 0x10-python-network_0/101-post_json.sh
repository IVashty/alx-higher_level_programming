
#!/bin/bash
# send a post request with a json file
curl -sXH POST "Content-Type: application/json" -d @"$2" "$1"
