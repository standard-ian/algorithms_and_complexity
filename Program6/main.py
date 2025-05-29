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

from graph import spread, breadth_first, Graph

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

    adj_list4 : dict = {
            "baz" : ["gimblog", "krauta", "frank"],
            "gimblog" : ["baz", "gloop", "krauta", "twack", "gerbil"],
            "gloop" : ["gimblog", "twack"],
            "fry" : ["krauta", "gerbil", "quack"],
            "krauta" : ["baz", "gimblog", "fry"],
            "twack" : ["gimblog", "gloop"],
            "frank" : ["baz"],
            "gerbil" : ["gimblog", "fry"],
            "quack" : ["fry", "fooper"],
            "fooper" : ["quack"]
        }

    adj_list3 = {
        1 : [2, 3],
        2 : [1, 3, 4],
        3 : [1, 2, 4, 5],
        4 : [2, 3, 5],
        5 : [3, 4]}


    # 1.
    '''
    print(f"\nList 1:\n{spread(adj_list, 8, 2)} levels spread. Expected: 3")
    print(f"\nThe graph as an adjacency list:")
    for _ in adj_list:
        print(f"{_} --> {adj_list[_]}")
    print(f"\nBreadth first traversal:")
    breadth_first(adj_list, 2)
    my_graph = Graph(adj_list)
    print(f"\n{my_graph}")

    # 2.
    print(f"\nList 2:\n{spread(adj_list2, 7, 1)} levels spread. Expcted: 2")
    print(f"\nThe graph as an adjacency list:")
    for _ in adj_list2:
        print(f"{_} --> {adj_list2[_]}")
    print(f"\nBreadth first traversal:")
    breadth_first(adj_list2, 2)
    my_graph2 = Graph(adj_list2)
    print(f"\n{my_graph2}")

    # 3.
    print(f"\nList 3:\n{spread(adj_list3, 3, 1)} levels spread. Expected: 2")
    print(f"\nThe graph as an adjacency list:")
    for _ in adj_list3:
        print(f"{_} --> {adj_list3[_]}")
    print(f"\nBreadth first traversal:")
    breadth_first(adj_list3, 1)
    my_graph3 = Graph(adj_list3)
    print(f"\n{my_graph3}")

    # 4.
    print(f"\nList 4:\n{spread(adj_list4, 9, "gimblog")} levels spread.")
    print(f"\nThe graph as an adjacency list:")
    for _ in adj_list4:
        print(f"{_} --> {adj_list4[_]}")

    my_graph4 = Graph(adj_list4)
    print(f"\n{my_graph4}")
    '''
    my_graph = Graph(adj_list4)
    my_graph.depth_first_display("baz")

if __name__ == "__main__":
    main()
