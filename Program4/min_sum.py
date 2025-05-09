#!/usr/bin/python3

####################################################################
# Ian Leuty & Stephen Feng
# ileuty@pdx.edu
# 4/24/2025
# CS350 Spring 2025
# Homework 4
#####################################################################
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
def naiive_rec(matrix, row, col) -> int:
    # ensure there is a valid matrix here
    if (len(matrix[row]) == 0):
        raise ValueError("Empty row present. Cannot find min descent")

    # base case:
    if (len(matrix[row]) == len(matrix[-1])):
        return matrix[row][col]

    bot = naiive_rec(matrix, row + 1, col)
    right = naiive_rec(matrix, row + 1, col + 1)

    # use min to determine the shorter of the paths upon return from both recursive calls
    return matrix[row][col] + min(bot, right)

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
def memo_rec(matrix, memo, row, col) -> int:
    # ensure there isn't a random "blank" row
    if (len(matrix[row]) == 0):
        raise ValueError("Empty row present. Cannot find min descent")

    # base case, value here has been updated and we don't need to re-recurse
    if (memo[row][col] != -1):
        return memo[row][col]

    # last row, path has been determined, just return the value in the matrix
    # so that is is added to the memoized total
    if (len(matrix[row]) == len(matrix[-1])):
        return matrix[row][col]

    # place cannot return yet, recurse further but update solutions stored in memo
    left = memo_rec(matrix, memo, row + 1, col)
    right = memo_rec(matrix, memo, row + 1, col + 1)

    memo[row][col] = matrix[row][col] +  min(left, right)

    # return this updated memo value
    return memo[row][col]

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

    matrix1 = [[2], [5, 4], [1, 4, 7], [8, 6, 9, 6]] # 14
    matrix2 = [[4], [4, 4], [4, 4, 4], [4, 4, 4, 4]] # 16
    matrix3 = [[6], [2, 1], [4, 1, 1], [1, 10, 9, 6]] #13
    matrix4 =[[3], [2, 4], [7, 2, 1], [4, 10, 1, 6]] #8
        # Basic triangle:
        #    2
        #   5 4
        #  1 4 7
    matrix5 = [[2], [5, 4], [1, 4, 7]] # 2->5->1 = 8

        # Larger triangle:
        #     3
        #    7 4
        #   2 4 6
        #  8 5 9 3
    matrix6 = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]] # 16
        # Triangle with negative values:
        #     -1
        #    2 -3
        #   1 -2 3
    matrix7 = [[-1], [2, -3], [1, -2, 3]]# -6
        # Triangle with zeros:
        #     0
        #    0 0
        #   0 0 0
    matrix8 = [[0], [0, 0], [0, 0, 0]] # 0
        # Single value triangle
    matrix9 = [[5]] # 5
        # Two rows triangle:
        #    1
        #   2 3
    matrix10 = [[1], [2, 3]] # 3

    cases : list = [matrix1, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7, matrix8, matrix9, matrix10]

    for i in cases:
        min_naiive = min_sum_naiive(i)
        min_memoized = min_sum_memo(i)
        min_tabulation = min_sum_tab(i)
        print("The Matrix:")
        for _ in i:
            print(_)
        print(f"NAIIVE: {min_naiive}\nMEMOIZED: {min_memoized}\nTABULATION: {min_tabulation}\n")


#####################################################################
if (__name__ == "__main__"):
    main()

'''
1. Describe how the original problem is built from smaller self-similar overlapping subproblems, and relate this back to the recursive formula for this problem.
    The original problem requires taking a look at the item directly below, and the item below and to the right, then deciding which is smaller.
    However, becuase the smallest path to the bottom is desired, the whole path has to be considered, not just the greedy approach to the next step.
    If we were to look at the second to bottom row however, then make this decison, we can be greedy, because once there is only one row, we've reached the bottom.
    So, when this sub-problem is reached, we can make a decision about which value is smaller (directly below or below and to the right), then essentially treat the second to last row as itself plus it's min descent.
    Returning back up the triangle, this process can just be repeated.

2. What is the time complexity (Big O) of each solution?
    The dyamic programming solutions (memo and tab) are both O(n) because they must touch every item in a triangle where each row is one longer than the previous and the first is only one item with no empty rows.
    Since the initial input is n items in a triangle arrangement, memoization and tabulation prevent the redundancies of recursion, meaning elements are not touched more than once in the worst case.

    The naive solution is slower because it has to touch certain elements multiple times unnecessarily.
    For every item starting with the second row, there is an item in the next row that it recurses on that is shared with it's neighbor.
    Because row 1 calls the function on each of it's "children" and those children call it on each of their's, but they share a child, we do 1 extra call at row 2, 2 on row 3, etc.
    So as we descend the triangle, we touch every element starting with the root (1) + next row (2) + next (3)...+height(h)
    This reduces to n(number of elements) = (height(height + 1)) / 2 -> 1/2 (height ^ 2 + height) -> height ^ 2,  by Gauss's formuala.
    At each level, the recursive calls double (2 at row 1, 4 at row 2, 8 at row 3, etc.) so the complexity is 2^height
    By taking sqrt(n) = squrt(height^2) -> height = sqrt(n), then plugging this into the complexity in terms of height, we get:
    O(2^sqrt(n)) complexity for the naive solution. This is not O(2^n) but it is still quite bad, and if the triangle is higher than 1 row (n >= 3) the complexity is quite bad.

3. Why do the Dynamic Programming solutions run so much faster than the Naiive Recursive version?
    The dynamic solutions are faster because they eliminate the need to repetetively recurse when subproblems overlap, by storing the value in another structure the first time it is found, then referencing that for future calls.
'''
