#!/usr/bin/python3
"""
take url and email send a POST request to the passed url
with the email as parameter the display body of response
"""

import requests
import sys

if __name__ == "__main__":
    request = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(request.text)
