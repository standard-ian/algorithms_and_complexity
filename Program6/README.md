To use the pytest suite for this program, create a venv and then run:
`pip install -r requirements.txt`

##### 1. What is the Big O time efficiency for your implementation?
    The main loop runs k times as we visit as many items as is specified by the function parameter, which takes O(k) time\\
    Within the first sub-loop, we itereate through the items adjacent to each node in the queue, which takes O(some fraction of n) time\\
    Then within the sub-loop, we access the visited set in O(1) time to determine if an item is to be added to the queue\\
    So, because we iterate through k total items in the order they are added to the queue, and at each one we itereate through it's adjacenct items, the complexity will be:\\
    O(k * (avg. adjacent)).


##### 2. What is an example of a worst case scenario that would cause your implementation to run in that Big O time complexity?
    A fully connected graph where the number to\_visit parameter is equal to the number of nodes - 1. When these values are equal, the traversal will touch the maximum number of items and levels.\\
    A fully connected graph would make the ratio of edges to nodes as high as possible.\\
    In addition, starting from a node with only 1 edge to it means that to reach the k (which is a max in this case, k = n - 1), more traversals will need to take place.\\
    It is important to note that a higher returned "levels" value does not necessarily mean the time complexity is worse. It is more a factor of the average adjacent items and the given k value.\\
    Because a key mechanic in the algorithm is a loop through the adjacency list every time a node is "visited" (popped from the queue),\\
    this average adjacency list length (which is proportional to the number of edges) is a useful metric on determining how the complexity scales.\\
    A fully connected graph will have the longest possible average adjacency list length, and having a number to visit equal to number of nodes (n = k) means we'll explore n nodes in the main loop,\\
    then at each node walk the longest possible chain of adjacent nodes looking for unvisited nodes.

##### 3. What is an example of a best case scenario for your implementation?
    A best case scenario would be a single central "hub" node with every other node connected only to this central node.\\
    In addition, the starting node matters. For example, if we start with the central node, everything else is found on level 1.\\
    However, if we start with a non-central node, only the central node is on level 1 relative to that starting point, and everything else is on level 2.\\
    An example of this would be test case 4 in the pytest suite.\\
    The reason for this is that the adjacency list has an average length of just less than 2 nodes. For 10 nodes, only 9 edges exist.

##### 4. Why does the Breadth First Search approach work well for this problem?
    Breadth first works well because the idea of sharing information with closest neighbors.\\
    These closes neighbors are represented by the adjacency list mapped to each item in the dictionary representing the graph.

##### 5. Do you think this can this be solved using Depth First Search?
    I think depth first search could work, we'd just have to compare the items to visit with the items visited differently, and increment level counters in a different way.\\
    The number of extra containers might be less, because we could just traverse to the first item in each dict entry's list to determine the next node to visit instead of using a queue.\\
    We'd have to track nodes visited as well while doing this, or at least the number of visited nodes in a counter to know when k is reached.\\
    Breadth first lends itself nicely to this problem, as it does finding a min path because it works with on the principle of dealing with all immediatly adjacent items before moving "deeper" or to a higher level of the graph.


