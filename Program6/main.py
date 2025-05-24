#!/usr/bin/python3

####################################################################
# Ian Leuty
# ileuty@pdx.edu
# 5/21/2025
# CS350 Spring 2025
# Homework 6
#####################################################################
# executable main
#####################################################################

from graph import spread, breadth_first

def main():
    adj_list2 : dict = {
            1 : [2, 3, 4],
            2 : [1, 5, 6],
            3 : [1, 7],
            4 : [1, 8, 9],
            5 : [2],
            6 : [2],
            7 : [3],
            8 : [4],
            9 : [4]}

    adj_list : dict = {
            1 : [2, 5, 7],
            2 : [1, 3, 5, 6, 8],
            3 : [2, 6],
            4 : [5, 8, 9],
            5 : [1, 2, 4],
            6 : [2, 3],
            7 : [1],
            8 : [2, 4],
            9 : [4, 10],
            10 : [9]
        }
    adj_list3 = {
        1 : [2, 3],
        2 : [1, 3, 4],
        3 : [1, 2, 4, 5],
        4 : [2, 3, 5],
        5 : [3, 4]}

    print(f"\nThe graph as an adjacency list:")
    for _ in adj_list:
        print(f"{_} --> {adj_list[_]}")

    print(f"\nBreadth first traversal:")
    breadth_first(adj_list, 2)
    print(f"\n{spread(adj_list, 8, 2)} levels spread.")

if __name__ == "__main__":
    main()
