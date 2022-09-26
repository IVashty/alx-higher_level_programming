#!/usr/bin/python3
# Task 0
print_list_integer = __import__("0-print_list_integer").print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

# task 1
element_at = __import__("1-element_at").element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

# Task 2
replace_in_list = __import__("2-replace_in_list").replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

# Task 3.
print_reversed_list_integer = __import__(
    "3-print_reversed_list_integer"
).print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

# task 4
new_in_list = __import__("4-new_in_list").new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

# task 5
no_c = __import__("5-no_c").no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

# task 6
print_matrix_integer = __import__("6-print_matrix_integer").print_matrix_integer

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
