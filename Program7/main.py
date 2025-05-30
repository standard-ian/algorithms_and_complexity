#!/usr/bin/python3
####################################################################
# Ian Leuty
# ileuty@pdx.edu
# 5/27/2025
# CS350 Spring 2025
# Homework 7
#####################################################################
# executable main
#####################################################################

from functions import islands

def main():
    matrix : list = [
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
    ]


    # while user wants to do more
    once_more : bool = True
    while (once_more):
        # get dimensions
        rows : int = int(input("\nCreating island map...\n\nNumber of rows?\n>"))
        columns : int = int(input("\nNumber of columns?\n>"))

        # while a valid matrix has not been entered
        valid : bool = False
        while (not valid):
            try:
                # init a matrix to all 0s
                matrix2 : list = [[0] * columns for row in range(rows)]

                print(f"\n{rows} x {columns} Matrix. Enter matrix values row by row, separated by white space\n")

                # get matrix values row by row
                for row in matrix2:
                    valid_row : bool = False
                    while (not valid_row):
                        raw_row = input(">")
                        # remove whitespace
                        raw_row = raw_row.split()

                        # if more items entered than
                        if (len(raw_row) != columns):
                            print(f"\nRow length should be {columns} items.")
                            print("Try entering the row again.")
                        else:
                            valid_row = True

                    # assign items to actual row in matrix
                    for item in range(rows):
                        row[item] = int(raw_row[item])

                # preview the map
                print("\nThe map:\n")
                for row in matrix2:
                    print(row)

                # compute islands and print result, break retry loop
                print(f"\nIslands in matrix: {islands(matrix2)}")
                valid = True

            # matrix was invalid, print error message
            except Exception as e:
                print(f"Error: {e}")

        # prompt user to do again
        once_more = again()

# get input if should do again
def again() -> bool:
    return True if (input("\nAgain? (y/n)\n>").upper() == 'Y') else False


if __name__ == "__main__":
    main()
