#!/usr/bin/env python3
# quiz 7
islower = __import__("7-islower").islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

# quiz 8
uppercase = __import__("8-uppercase").uppercase

uppercase("best")
uppercase("Best School 98 Battery street")

# quiz 9
print_last_digit = __import__("9-print_last_digit").print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

# quiz 10
add = __import__("10-add").add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

# quiz 11
pow = __import__("11-pow").pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

# quiz 12
fizzbuzz = __import__("12-fizzbuzz").fizzbuzz

fizzbuzz()
print("")
