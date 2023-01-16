#!/bin/bash
#Sets a custom header in a get request with curl
curl -s -H "X-School-User-Id: 98" "$1"
