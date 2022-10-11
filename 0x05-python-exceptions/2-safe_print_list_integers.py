#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    x_elements = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            x_elements += 1
        except (ValueError, TypeError):
            element += 1
            continue
    print("")
    return x_elements
