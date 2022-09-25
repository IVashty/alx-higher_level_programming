#!/usr/bin/env python3
def print_last_digit(number):
    last_number = number % 10 if number >= 0 else -number % 10
    print(f"{last_number}", end="")
    return last_number
