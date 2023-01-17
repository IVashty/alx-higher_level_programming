
#!/bin/bash
# send a post request with a json file
curl -sX POST  "Content-Type: application/json" -d @"$2" -H "$1"
