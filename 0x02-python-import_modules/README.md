# TASKS:
0. Write a program that imports functions from the file ~~calculator_1.py~~, does some Maths, and prints the result.
    - Do not use the function `print` (with string format to display integers) more than 4 times
    - You have to define:
         - the value 10 to a variable a
         - the value 5 to a variable b
         - and use those two variables only, as arguments when calling functions (including print)
    - a and b must be defined in 2 different lines: a = 10 and another b = 5
    - Your program should call each of the imported functions. See example below \ for format
    - the word `calculator_1` should be used only once in your file
    - You are not allowed to use `* for importing` or `__import__`
    - Your code should not be executed when imported

1. A program that imports functions from the file calculator_1.py, does some \ Maths,  and prints the result.

    Do not use the function print (with string format to display integers) more \ than 4 times
    You have to define:
        the value 10 to a variable a
        the value 5 to a variable b
        and use those two variables only, as arguments when calling functions \(including print)
    a and b must be defined in 2 different lines: a = 10 and another b = 5
    Your program should call each of the imported functions. See example below \for format
    the word `calculator_1` should be used only once in your file
    You are not allowed to use `*` , `for importing` or `__import__`
    Your code should not be executed when imported

2. A  program that prints the number of and the list of its arguments.

    The output should be:
        Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
        : (or . if no arguments were passed) followed by
        a new line, followed by (if at least one argument),
        one line per argument:
            the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
    Your code should not be executed when imported
    The number of elements of `argv` can be retrieved by using: `len(argv)`
    You do not have to fully understand lists yet, but imagine that `argv` can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

3. A program that prints the result of the addition of all arguments.

    The output should be the result of the addition of all arguments, followed by a new line
    You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
    Your code should not be executed when imported


4. A  a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

    You should print one name per line, in alpha order
    You should print only names that do not start with `__`
    Your code should not be executed when imported
    Make sure you are running your code in Python3.8.x (hid`den_4.pyc` has been compiled with this version)
 
 5. A  program that imports the variable a from the file variable_load_5.py and prints its value.

    You are not allowed to use `*` ,`for importing` or `__import__`
    Your code should not be executed when imported

6. A program that imports all functions from the file calculator_1.py and handles basic operations.

    Usage: `./100-my_calculator.py` a operator b
        If the number of arguments is not 3, your program has to:
            print Usage: `./100-my_calculator.py <a> <operator> <b>` followed with a new line
            exit with the value 1
        operator can be:
            + for addition
            - for subtraction
            * for multiplication
            / for division
        If the operator is not one of the above:
            print Unknown operator. Available operators: +, -, `*` and / followed with a new line
            exit with the value 1
        You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
        The result should be printed like this: `<a> <operator> <b> = <result>`, followed by a new line
    You are not allowed to use `*` for importing or `__import__`
    Your code should not be executed when imported

7. A program that prints #pythoniscool, followed by a new line, in the standard output.

    Your program should be maximum 2 lines long
    You are not allowed to use `print` or` eval` or `open` or `import sys` in your file `101-easy_print.py`

8. Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode.
Use [Python bytecode](https://alx-intranet.hbtn.io/rltoken/FMdg7W8NKJZKRuFGG8mzmg)

9. A program that prints the alphabet in uppercase, followed by a new line.

    Your program should be maximum 3 lines long
    You are not allowed to use:
        any loops
        any conditional statements
        `str.join()`
        any string literal
        any system calls


