#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    addition = len(sys.argv)
    if addition == 1:
        print("{} arguments.".format(addition - 1))
    elif addition == 2:
        print("{} argument:".format(addition - 1))
    else:
        print("{} arguments:".format(addition - 1))
    for i in range(1, addition):
        print("{}: {}".format(i, sys.argv[i]))
