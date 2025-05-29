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
    print(f"Islands in matrix: {islands(matrix)}")

if __name__ == "__main__":
    main()
