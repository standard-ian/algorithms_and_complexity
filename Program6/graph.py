####################################################################
# Ian Leuty
# ileuty@pdx.edu
# 5/21/2025
# CS350 Spring 2025
# Homework 6
#####################################################################
# function implementation of graph traversal functions
#
# breadth_first:
#   traverses the nodes of a graph given a starting point and prints their values
#   not a part of the assignemnt, but useful to get the basics of breadth first traversal
#
#
# spread:
#   assume you have an unweighted, undirected, simple graph represented as either an adjacency matrix or an adjacency list.
#   the graph has n total nodes, and each node is a unique integer from 0 to n.
#   the graph itself models a Social Network of people, where each node represents a single person in the network.
#   each edge between two people represents a connection, and information can pass between two connected people.
#   given some source node, develop a function that uses the Breadth First Search (BFS) traversal algorithm
#   determine how quickly information can spread from that source node to k-number of other people.
#   speed of spread is determined by how many levels of connection from the starting node we have to go before reaching a total of k-number of other people.
#
# documentation video includes:
#   1. what is the big o time efficiency for your implementation?
#   2. what is an example of a worst case scenario that would cause your implementation to run in that big o time complexity?
#   3. what is an example of a best case scenario for your implementation?
#   4. why does the breadth first traversal approach work well for this problem?
#   5. do you think this can this be solved using depth first traversal?
#
#####################################################################

#####################################################################
# spread function
#####################################################################
# parameters:
#   1. an adjacency list in the form of a dictionary,
#   2. a number of nodes that should be visited during the runtime of the function
#   3. a node value from which to start
# returns:
#   levels of connection it takes to reach a given number of people (speed of spread)
#####################################################################
def spread(adj_list : dict, to_visit : int, start : int) -> int:
    # set to track visited items
    # add an item when it has been visited
    visited = set()

    # create a queue of tuples (node_value, level_in_relation_to_start)
    levels : list = [(start, 0)]
    # current node tracker
    current : int = None
    # current node's level tracker
    level : int = 0

    # don't count the start node as a part of the "spread"
    # but mark it as visited and append it to the next level queue.
    # when it is popped, that will be exploring level 0
    nodes_visited : int = 0

    # add the start point to the visited set
    # and append a tuple of its value and level to the end of the levels queue
    visited.add(start)

    # main loop, runs at most k (to_visit) times: O(k)
    while (levels and nodes_visited < to_visit):
        # pop the next node value and it's level in relation to the start
        current, level = levels.pop(0)

        # increase the count of nodes visited (not counting the starting node)
        if (current != start):
            nodes_visited += 1

        # for each item in the current node's adjacency list
        # runs for an amount of time equal to the average length of each list in the adjacency list O(l)
        for neighbor in adj_list[current]:
            # if the neighbor is not visited
            # iterates through the visited array, iterates between 1 and k times
            if (neighbor not in visited):
                # append it to the levels queue, marking it as at (current_level + 1)
                # and mark it as visited
                levels.append((neighbor, level + 1))
                visited.add(neighbor)

    # once the queue is empty or the nodes_visited = k (to_visit)
    # the level (speed of spread) is now known, return it.
    return level

####################################################################
# basic breadth first traversal
#####################################################################
# base breadth first traversal function
# displays nodes in the order visited
# params:
#   a graph as an adjacency list
#   a starting node
# returns:
#   None
#####################################################################
def breadth_first(adj_list : dict, start : int) -> None:
    total_nodes : int = len(adj_list)
    visited : dict = {}
    for _ in adj_list:
        visited[_] = False
    queue : list = []

    queue.append(start)
    visited[start] = True

    while (queue):
        current : int = queue.pop(0)

        print(current)

        for _ in adj_list[current]:
            if (visited[_] == False):
                queue.append(_)
                visited[_] = True

####################################################################
# edges
####################################################################
# find the shortest path distance between two specific nodes
# params:
#   start node
#   end node
# returns:
#   number of edges in shortest path between start and end
####################################################################
def edges(adj_list: dict, start: int, end: int) -> int:
    # handle edge case where start equals end
    if (start == end):
        return 0

    # check if start and end nodes exist in the graph
    if (start not in adj_list or end not in adj_list):
        raise ValueError("Start or end item not present.")

    # create a set to track visited nodes (more efficient than dict)
    visited = set()

    # queue stores tuples of (node, distance_from_start)
    queue = [(start, 0)]
    visited.add(start)
    current_node = None

    # while there is a queue of items and we've not reached the end
    while (queue and current_node != end):
        current_node, current_distance = queue.pop(0)

        # base case: if we're at the end node, return the current distance
        #if (current_node == end):
            #return current_distance

        # check all neighbors of the current node
        for neighbor in adj_list[current_node]:

            # if neighbor hasn't been visited, add it to queue w updated distance
            if (neighbor not in visited):
                visited.add(neighbor)
                queue.append((neighbor, current_distance + 1))

    return current_distance

