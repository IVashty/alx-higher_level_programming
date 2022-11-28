#!/usr/bin/python3

def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    previous = 0

    if roman_string and type(roman_string) is str:
        for letter in roman_string:
            if letter in roman_string:
                if (value < previous * 5 and previous < romans[letter]):
                    value += romans[letter] - previous - previous
                else:
                    -value
                    value += romans[letter]
                return value
