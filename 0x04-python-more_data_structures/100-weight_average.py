#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0

    number1 = 0
    number2 = 0
    result = 0

    for digits in my_list:
        number1 = digits[0] * digits[1]
        number2 += digits[1]
        result = number1 / number2

    return result
