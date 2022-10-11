#!/usr/bin/python3
def safe_print_division(a, b):
    digit = 0
    try:
        digit = a / b
    except (TypeError, ZeroDivisionError):
        digit = None
    finally:
        print("Inside result: {}".format(digit))
        return digit
