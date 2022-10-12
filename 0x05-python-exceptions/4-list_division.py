#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lists = []
    for element in range(list_length):
        try:
            lists.append(my_list_1[element] / my_list_2[element])
            continue
        except ZeroDivisionError:
            print("division by 0")
            lists.append(0)
        except TypeError:
            print("wrong type")
            lists.append(0)
        except IndexError:
            print("out of range")
            lists.append(0)
        finally:
            pass
    return lists
