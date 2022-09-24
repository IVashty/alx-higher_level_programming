#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = number % 10 if number > 0 else int(repr(number)[-1]) * -1
if last_digit > 5:
    print(
        "last digit of {} is {} and is greater than 5".format(
            number, last_digit
        )
    )
elif last_digit == 0:
    print("last digit {} is {} is 0".format(number, last_digit))
elif last_digit < 6:
    print(
        "last digit is {} is {} is less than 6 and not 0".format(
            number, last_digit
        )
    )
