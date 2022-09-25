#!/usr/bin/python3
def uppercase(str):
    for v in range(len(str)):
        if ord(str[v]) <= 122 and ord(str[v]) >= 97:
            ascii_no = 32
        else:
            ascii_no = 0
            print("{:c}".format(ord(str[v]) - ascii_no), end="")
    print()
