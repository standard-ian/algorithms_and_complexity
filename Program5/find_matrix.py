#!/usr/bin/python3

####################################################################
# Ian Leuty
# ileuty@pdx.edu
# 5/9/2025
# CS350 Spring 2025
# Homework 5
#####################################################################
# Solution to find if an item is present in a matrix of at most 100
#   1. Target cannot be greater than 100000
#   2. Values in the matrix cannot be less than 0.001
#   3. Matrix must have a height of at least 1
#   4. Rows must contain at most 100 items
#   5. Solution must run w/ O(log(m x n)) complexity
#
# To achieve logarithmic complexity, where the n is the number of items in the "area" of the square matrix, we'll use interval halving and recursion
# First, find a midpoint in the rows and determine if the target is:
#   1. in that row
#   2. in the rows above
#   3. in the rows below
# At each recursive call, we'll bisect the matrix rows and enter a new frame w/ a smaller matrix (the rows above or below the midpoint)
# Alternatively, if the target is found to be in the row of the midpoint, or if the smaller matrix consists of only 1 row, a new recursive binary search function can be called.
# This function will operate similary, but on a single list, the desired row passes as a parameter from the initial function.
# Because we recurse on the height first, using a binary search pattern we traverse all the values in the height (m) in logarithmic time.
# Then, We'll eventually recurse on a single row of "n" items applying the same binary search logic, again resulting in logarithmic time.
# However, the find_row function will only be called once, not on every row.
# So, I believe the complexity will actually be O(log m) + O(log n).
#####################################################################

#initial recusrive function to find the row of the target
def find(matrix : list, target : int | float) -> bool:
    # get the number of rows
    matrix_rows : int = len(matrix)

    # check for inappropriate target, len, min val
    if (matrix_rows == 0 or len(matrix[0]) == 0):
        raise ValueError("Invalid matrix: Cannot be empty")
    if (target > 100000):
        raise ValueError("Invalid target: must equivalent to 100,000 or less")
    if (matrix[0][0] < 0.001):
        raise ValueError("Invalid matrix: min value is less than one ten-thousandth")
    if (matrix_rows > 100):
        raise ValueError("Invalid matrix: greater than 100 rows")

    # establish a midpoint
    mid : int = matrix_rows // 2

    # check if there is anything here at this index
    if (len(matrix[mid]) == 0):
        # if there is nothing, advance one row
        return find(matrix[1:], target)

    # determine in the target is in the row at mid
    if (matrix_rows == 1 or (target < matrix[mid][-1] and target > matrix[mid][0])):
        return row_find(matrix[mid], target)

    # if not, determine if it is in the rows below
    if (target >= matrix[mid][0]):
        return find(matrix[mid:], target)
    # or above
    return find(matrix[:mid], target)

####################################################################

#recursively search the row for the target
def row_find(row : list, target : int | float) -> bool:
    # get the number of items in the row
    row_length : int = len(row)

    # if there's only one item and it is not the target, the target is not in the matrix
    if (row_length == 1):
        if (row[0] != target):
            return False
        else:
            return True

    # establish a mid point and grab the value there to reference
    mid : int = row_length // 2
    mid_val : int = row[mid]

    # if the target is there, it's been found.
    if (mid_val == target):
        return True

    # if not, determine if it is after the middle value
    if (target > mid_val):
        return row_find(row[mid:], target)
    # or before
    return row_find(row[:mid], target)

####################################################################

def main():
    matrix : list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    target : int = int(input(f"Here is the matrix:\n{matrix}\n\nEnter a target value to search for\n>"))

    if (find(matrix, target) == True):
        print(f"{target} was found!")
    else:
        print(f"{target} is not here...")

####################################################################
if __name__ == "__main__":
    main()
