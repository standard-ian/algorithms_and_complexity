####################################################################
# Ian Leuty
# ileuty@pdx.edu
# 5/27/2025
# CS350 Spring 2025
# Homework 7
####################################################################

####################################################################
# "islands" function
####################################################################
# function implementation:
#   given a matrix of only 1s and 0s that is at most 300 x 300 items,
#   return the number of "islands" of 1s (i.e. groups of "1"s unconnected to any other "1")
#
# params:
#   an n x m matrix of only 1s and 0s
# returns:
#   total number of isolated groups of "1"s.
####################################################################
def islands(matrix : list):
    # check all initial constraints are met:
    # check there are 300 or less rows
    if (len(matrix) > 300):
        raise ValueError("Matrix must be 300 \"rows\" or less")
    # check there are 300 or less columns
        if (len(row) > 300):
            raise ValueError("Matrix must be 300 \"columns\" or less")
    # ensure matrix is valid for the finding islands of "1"s
    for row in matrix:
        for col in row:
            if (int(col) != 1 and int(col) != 0):
                raise ValueError("Matrix must consist of 1s and 0s only")

    # get length of rows and length of columns
    rows, cols = len(matrix), len(matrix[0])

    # create a matrix to mark visited items (memoization)
    visited = [[False] * cols for _ in range(rows)]

    # count for number of islands
    islands : int = 0

    # inline recursive function to recurse in all directions from a given coordinate until:
    #   1. out of bounds of matrix
    #   2. visited item is encountered (memoization efficiency)
    #   3. a 0 is encountered
    # inline, so visited matrix, original matrix, rows, cols, still in scope
    def depth_first(r, c):
        # base case to stop when one of the above conditions is met
        if (r < 0 or r >= rows or c < 0 or c >= cols
            or visited[r][c]
            or matrix[r][c] == 0):
            return

        # if we're here, the current item is:
        #   1. in bounds
        #   2. not yet seen
        #   3. not a 0
        # mark this item as visited
        visited[r][c] = True

        # travel out from this point in all directions
        depth_first(r + 1, c)
        depth_first(r - 1, c)
        depth_first(r, c + 1)
        depth_first(r, c - 1)

    # walk the matrix calling the recursive spreading function on every new unvisited "land"
    # since all groups are tied to an item that has been marked visited...
    for row in range(rows):
        for col in range(cols):
            # ...if an item is previously visited and is a 1,
            # it belongs to a different island...
            if (matrix[row][col] == 1 and not visited[row][col]):
                # ...if not, it's a new group to be counted
                depth_first(row, col)
                islands += 1

    return islands











