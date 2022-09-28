#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for int in range(len(my_list)):
        if my_list[int] == search:
            newlist.append(replace)
        else:
            newlist.append(my_list[int])
    return newlist
