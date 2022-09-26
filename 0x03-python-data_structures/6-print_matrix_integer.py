#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ind in range(len(matrix)):
        for int in range(len(matrix[ind])):
            if int != 0:
                print(" ", end="")
            print("{:d}".format(matrix[ind][int]), end="")
        print()
