"""
Module name is matrix_divided
It returns the result of the division of all the items in the matrix by  `div`
It takes matrix composed of only integers and floats
otherwise a
TypeError is raised.
"""


def matrix_divided(matrix, div):
    """
    Each element of `matrix` is divided by `div`

    matrix_divided:
    checks tos see
    - if div is the correct type and is not zero
    - if matrix is well-formed ,copy it and divide then return the new matrix

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    wrong_type = "matrix must be a matrix (list of lists) of integers/floats"
    wrong_size = "Each row of the matrix must have the same size"
    new_matrix = []
    if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
        raise TypeError(wrong_type)
    previous = len(matrix[0])

    try:
        for count, row in enumerate(matrix):
            if not isinstance(row, list):
                raise TypeError(wrong_type)
            if len(row) != previous:
                raise TypeError(wrong_size)
            previous = len(row)
            new_matrix.append(row[:])
            for val, item in enumerate(row):
                if not isinstance(item, (int, float)):
                    raise TypeError(wrong_type)
                new_matrix[count][val] = round(item / div, 2)
    except Exception:
        raise
    else:
        return new_matrix
