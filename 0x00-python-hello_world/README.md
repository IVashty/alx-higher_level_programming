# Requirements
## Python Scripts

    - Allowed editors: vi, vim, emacs
    - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    - All your files should end with a new line
    - The first line of all your files should be exactly #!/usr/bin/python3
    - A README.md file at the root of the repo, containing a description of the repository
    - A README.md file, at the root of the folder of this project, is mandatory
    - Your code should use the pycodestyle (version 2.8.*)
    - All your files must be executable
    - The length of your files will be tested using wc

## Shell Scripts

    - Allowed editors: vi, vim, emacs
    - All your scripts will be tested on Ubuntu 20.04 LTS
    - All your scripts should be exactly two lines long (wc -l file should print 2)
    - All your files should end with a new line
    - The first line of all your files should be exactly #!/bin/bash
    - All your files must be executable

C Scripts

    - Allowed editors: vi, vim, emacs
    - All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
    - All your files should end with a new line
    - Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
    - You are not allowed to use global variables
    - No more than 5 functions per file
    - In the following examples, the main.c files are shown as examples. 
    - You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
    - The prototypes of all your functions should be included in your header file called lists.h
    - Don’t forget to push your header file
    - All your header files should be include guarded

### TASKS:
0. Write a Shell script that runs a Python script.
        Saving the python file name under the enviroment variable `$PYFILE`

1. Write a Shell script that runs Python code.

2. Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.  -use the function`print`
3. Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line
4. Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
5. Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
6. Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
7. Complete this source code

    - You can find the source code here
    - You are not allowed to use any loops or conditional statements
    - Your program should be exactly 8 lines long
    word_first_3 should contain the first 3 letters of the variable word
    - word_last_2 should contain the last 2 letters of the variable word
    - middle_word should contain the value of the variable word without the first and last letters
8. Complete this source code to print object-oriented programming with Python, followed by a new line.

    - You can find the source code here
   - You are not allowed to use any loops or conditional statements
   - Your program should be exactly 5 lines long
   - You are not allowed to create new variables
   - You are not allowed to use string literals


9. && 10. Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

   - Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)
11. Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

    - Use the function write from the sys module
    - You are not allowed to use print
    - Your script should print to stderr
    - Your script should exit with the status code 1
12. Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
13. Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:(tip:python bytecode)

  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE



