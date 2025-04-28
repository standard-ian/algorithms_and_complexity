#!/usr/bin/python3

####################################################################
# Ian Leuty & Stephen Feng
# ileuty@pdx.edu
# 4/24/2025
# CS350 Spring 2025
# Homework 4
#####################################################################
# The problem is to find the smallest sum in a descent from the triangles apex to its base through a sequence of adjacent numbers
# Implement three solutions to this problem:
#
#     1. The Naiive Recursive solution that does NOT utilize Dynamic Programming
#     2. A recursive, Memoized Dynamic Programming solution
#     3. An iterative, Tabulated Dynamic Programming solution
#
# Note: a Greedy approach will not work for this problem
# You may write all three solutions in a single code file (where each solution is a separate function)
#####################################################################

# naiive recurive solution (no dynamic programming)
def min_sum_naiive(matrix) -> int:
    # if there are no rows in the matrix, invalid input - raise error
    if (len(matrix) == 0):
        raise ValueError("Empty matrix")
    #call recursive function
    return naiive_rec(matrix, 0, 0)

# recursive naiive (non-dynamic) function
def naiive_rec(matrix, row, index) -> int:
    # ensure there is a valid matrix here
    if (len(matrix[row]) == 0):
        raise ValueError("Empty row present. Cannot find min descent")

    # base case:
    if (len(matrix[row]) == len(matrix[-1])):
        return matrix[row][index];

    # use min to determine the shorter of the paths upon return from both recursive calls
    return min(naiive_rec(matrix, row + 1, index), naiive_rec(matrix, row + 1, index + 1)) + matrix[row][index]

#####################################################################


# memoized, recursive, dynamic programming solutuion
def min_sum_memo(matrix) -> int:
    # boilerplate exceptions
    matrix_len = len(matrix)

    if (matrix_len == 0):
        raise ValueError("Empty matrix")

    # create a matrix of all '-1' sized to the original matrix
    memo = [[-1] * (len(matrix[-1])) for _ in range (len(matrix))]

    # call recursive function with the memo
    return memo_rec(matrix, memo, 0, 0)

# recursive, memoized function
def memo_rec(matrix, memo, row, index):
    # ensure there isn't a random "blank" row
    if (len(matrix[row]) == 0):
        raise ValueError("Empty row present. Cannot find min descent")

    # base case, value here has been updated and we don't need to re-recurse
    if (memo[row][index] != -1):
        return memo[row][index]

    # last row, path has been determined, just return the value in the matrix
    # so that is is added to the memoized total
    if (len(matrix[row]) == len(matrix[-1])):
        return matrix[row][index]

    # place cannot return yet, recurse further but update solutions stored in memo
    memo[row][index] = matrix[row][index] +  min(memo_rec(matrix, memo, row + 1, index), memo_rec(matrix, memo, row + 1, index + 1))

    # return this updated memo value
    return memo[row][index]

#####################################################################

# Tabulation
def min_sum_tab(matrix) -> int:
    size = len(matrix)
    if (size == 0):
        raise ValueError("Empty matrix")

    result = []
    # Fill a 2D Array with -1, but copy the last row.
    for i in range(len(matrix)):
        if (len(matrix[i]) == 0):
            raise ValueError("Empty row present. Cannot find min descent")

        result.append([])
        if(i != size-1):
            for j in range(size):
                result[i].append(-1)
        else:
            for j in range(size):
                result[i].append(matrix[i][j])

    # print(result)

    # Start at the second last row, and calculate bottom up
    # The "minimum" value at row, col is itself + the minimum of the bottom two
    row = len(matrix)-2
    col = 0

    while row >= 0:
        col = 0
        while col <= row:
            result[row][col] = matrix[row][col] + min(result[row+1][col],
                                                    result[row+1][col+1])
            col += 1
        row -= 1

    # print(result)

    return result[0][0]

#####################################################################
def main():
    # TODO This isn't 4 by 4 matrix, it's jagged..
    matrix1 = [[2], [5, 4], [1, 4, 7], [8, 6, 9, 6]]
    print(f"The minumum sum descent (naiive solution) is: {min_sum_naiive(matrix1)}")
    print(f"The minumum sum descent (memoized solution) is: {min_sum_memo(matrix1)}")
    print(f"The minumum sum descent (tabulated solution) is: {min_sum_tab(matrix1)}")

#####################################################################
if (__name__ == "__main__"):
    main()
