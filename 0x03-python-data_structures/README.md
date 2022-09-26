### TASKS:
----------------

0. Write a function that prints all integers of a list.

    -Prototype: `def print_list_integer(my_list=[]):`
    - Format: one integer per line. See example
    - You are not allowed to import any module
    - You can assume that the list only contains integers
    - You are not allowed to cast integers into strings
    - You have to use `str.format()` to print integers

1. Write a function that retrieves an element from a list like in C.
    - Prototype: `def element_at(my_list, idx):`
    - If `idx` is negative, the function should return None
    - If `idx` is out of range (> of number of element in my_list), the function should return None
    - You are not allowed to import any module
    - You are not allowed to use try/except

2. Write a function that replaces an element of a list at a specific position (like in C).
   - Prototype: `def replace_in_list(my_list, idx, element):`
    - If `idx` is negative, the function should not modify anything, and returns the original list
    - If `idx` is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
    - You are not allowed to import any module
   - You are not allowed to use try/except

3. Write a function that prints all integers of a list, in reverse order.
    - Prototype: `def print_reversed_list_integer(my_list=[]):`
   - Format: one integer per line. See example
   - You are not allowed to import any module
    - You can assume that the list only contains integers
   - You are not allowed to cast integers into strings
   - You have to use `str.format()` to print integers

4. Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
    - Prototype: `def new_in_list(my_list, `idx`, element):`
    - If `idx` is negative, the function should return a copy of the original list
    - If `idx` is out of range (> of number of element in my_list), the function should return a copy of the original list
    - You are not allowed to import any module
    - You are not allowed to use try/except
5. Write a function that removes all characters c and C from a string.
    - Prototype: `def no_c(my_string):`
    - The function should return the new string
    - You are not allowed to import any module
    - You are not allowed to use `str.replace()`

6. Write a function that prints a matrix of integers.
    - Prototype: `def print_matrix_integer(matrix=[[]]):`
    - Format: see example
    - You are not allowed to import any module
    - You can assume that the list only contains integers
    - You are not allowed to cast integers into strings
    - You have to use `str.format()` to print integers
7. Write a function that adds 2 tuples.
    - Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
    - Returns a tuple with 2 integers:
        - The first element should be the addition of the first element of each argument
        - The second element should be the addition of the second element of each argument
    - You are not allowed to import any module
    - You can assume that the two tuples will only contain integers
    - If a tuple is smaller than 2, use the value 0 for each missing integer
    - If a tuple is bigger than 2, use only the first 2 integers



