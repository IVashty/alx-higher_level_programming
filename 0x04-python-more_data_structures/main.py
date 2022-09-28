#!/usr/bin/python3
# Task 0
square_matrix_simple = __import__("0-square_matrix_simple").square_matrix_simple

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

# Task 1
search_replace = __import__("1-search_replace").search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
