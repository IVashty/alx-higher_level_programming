#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

    lists = dir()
    for i in range(0, len(lists)):
        if lists[i][0:2] != "__":
            print("{}".format(lists[i]))
