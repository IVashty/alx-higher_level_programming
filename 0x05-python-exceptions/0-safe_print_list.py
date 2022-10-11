#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    x_elements = 0
    for element in range(x):
        try:
            print("{}".format(my_list[element]), end="")
            x_elements += 1
        except IndexError:
            pass
    print("")
    return x_elements
