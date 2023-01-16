#!/bin/bash
# size of the body of the response server will accept
curl -s -I "$1" | grep Allow | awk -F ": " '{print $2}'
