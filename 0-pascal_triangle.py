#!/usr/bin/python3
'''Generates Pascal's Triangle up to the nth row.
'''


def pascal_triangle(n):
    ''' - The function returns an empty list if n <= 0 or if n is not an integer.
    - The output is a list of lists, where each inner list represents a row of Pascal's Triangle.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
