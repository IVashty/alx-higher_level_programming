#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    results_added = 0
    for i in range(1, len(sys.argv)):
        results_added += int(sys.argv[i])
    print("{}".format(results_added))
