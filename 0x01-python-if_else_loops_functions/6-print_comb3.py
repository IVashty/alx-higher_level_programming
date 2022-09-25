#!/usr/bin/python3
for v in range(0, 9):
    for k in range(v + 1, 10):
        if v == 8:
            print("{}{}".format(i, k))
        else:
            print("{}{}".format(i, k), end=", ")
