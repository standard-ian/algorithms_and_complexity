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


    rows : int = int(input("Creating island map...\n\nNumber of rows?\n\033[1;34;5m>\033[0;0m"))
    columns : int = int(input("Creating island map...\n\nNumber of columns?\n\033[1;34;5m>\033[0;0m"))

    matrix2 : list = [[0] * columns for row in range(rows)]

    print("Enter matrix values\n")

    for row in matrix2:
        raw_row = input(">")
        raw_row = raw_row.split()
        for item in range(rows):
            row[item] = int(raw_row[item])

    print("The map:\n")
    for row in matrix2:
        print(row)

    print(f"Islands in matrix: {islands(matrix2)}")

if __name__ == "__main__":
    main()
