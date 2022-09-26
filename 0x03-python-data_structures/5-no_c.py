#!/usr/bin/python3
def no_c(my_string):
    ind = 0

    new_string = my_string[:]

    for str in range(len(my_string)):
        if (my_string[str] == "c") or (my_string[str] == "C"):
            new_string = (new_string[: (str - ind)]) + (my_string[(str + 1) :])
            ind += 1
    return new_string
