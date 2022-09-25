#!/usr/bin/python3
def uppercase(str):
    alist = list(str)
    for v in range(len(str)):
        if ord(alist[v]) <= 122 and ord(alist[v]) >= 97:
            alist[v] = chr(ord(alist[v]) - 32)
        else:
            alist = 0
            print("{}".format(("").join(alist)))
    print()
