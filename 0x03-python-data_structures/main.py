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

# task 7
add_tuple = __import__("7-add_tuple").add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1,)))
print(add_tuple(tuple_a, ()))

# task 8
multiple_returns = __import__("8-multiple_returns").multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

# task 9
max_integer = __import__("9-max_integer").max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

# task 10
divisible_by_2 = __import__("10-divisible_by_2").divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print(
        "{:d} {:s} divisible by 2".format(
            my_list[i], "is" if list_result[i] else "is not"
        )
    )
    i += 1

# task 11
delete_at = __import__("11-delete_at").delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
