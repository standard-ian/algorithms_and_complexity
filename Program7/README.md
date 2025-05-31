### Program 7
Run `main.py` for interactive testing.
Run pytest to test exception handling and 6 parametrized test cases.

##### How Does it Work?
The function first checks to make sure the matrix contains all 1s and 0s and that is its an even m x n rectangle where m and n are less than or equal to 300.

Then row and column sizes are established, as well as a variable to track the number of "islands".

A "visited matrix" is created. It is equal in size to the parameter matrix and in ininially mapped "False" to all "locations".

A recursive function is defined within. By defining it within, we reduce the number of arguments from 6 to 2, imporving readability. Now the only parameters needed are the ones actually performing the recursion, a row (r) and column (c).

The parameter matrix, the visited matrix, as well as the column and row bounds are still in scope and the matrices are mutable, so they can be elimintated from the argument list.

The recursive function simply recurses in all 4 possible directions that could expand the island, marking items visited as it touches them, until it hits a border, a 0 (water), or a visited item.

The rest of the main function just uses nested for loops to step through every item in the parameter matrix. If an item is unvisited, the recursive function is called on that coordinate.

"Islands" are counted every time the linear main nested loop encounters a new unvisited item. This works because the recursive function can only "visit" items that are connected to the start point by a valid path of 1's.

Because the items are marked visited by the recursive function and updated in real time before the main loop travels to the next item, if a new unvisited "1" item is encountered by the main loop, we know it is not connected to any previously counted island and we can increment the island counter.

##### Does it utilize a known algorithm, and if so, which one?
Algorithms used were recursive memoization of an identical visited matrix, as well as the concept of depth first search.
The depth first approach uses a nested loop to walk through the matrix one item at a time. It calls a recursive function that just travels depth in terms of immidiate adjacency to the current item (up, down, left, or right) instead of "traveling" to the node mapped to the 1 in the current row, memoizing the visited areas as it does so.

##### Why choose this approach?
I chose this approach because because it incorporated a few elements that we've covered this term. There was potential for a lot of wastefu recursion given te 4 recursive calls in the recursive function, so using a separare container to mark visited items and avoid re-visiting saved a lot of time and makes the parsing of islands a lot easier to understand and define in code.

##### What was your initial idea and how did it differ?
My initial idea was to make a dictionary of coordinates that were connected and mapped to the "island number" they are a part of.

This basically led to me making various different representations of the initial matrix that didn't get me any closer to the solution.

Once I studied the depth first algorithm for an adjacency matrix, the algorithm really just needed to be redefiend in terms of how nodes are visited (by position adjacency, rather than which index of the main matrix they are a part of).

Visited nodes are also marked using a matrix, because every item in the matrix is now sort of a unique point rather than a "pointer", if you will, to a real node.


##### What is the Big O for this solution?
Fixed O(m x n) (rows x cols) to check if matrix is valid format (1/0 only rectangle)

Fixed O(m x n) again to travel the entire matrix. Checking if items are visited or not.

Variable (max O(m x n)) time to recursively memoize. Only touch each item once,

but has no effect on the previous double for loop.

Some coefficient of O(m x n) overall. Every square needs to be explored.

Not sure it can be optimized much beyond O(m x n) overall complexity.

##### Discuss Best and Worst Case
Assuming the matrix height is m and the width is n,

While the initial parts of the function step through the matrix in m x n time to check it for validity, touching every item, they are lower or equivalent order to the main body.

The main function nested loop will always have O(m x n) complexity because it has to touch every item to check it it is a 1 or 0, and if it is visited.

Its call to the recursive function creates an additional dimenstion of complexity that varies based on how the matrix is arranged. It will recurse deeper the more connected items there are. For a matrix of all 1's, the recursive function will also touch every item. However, it will only do this once, as it's base case prevents it from recursing on a coordinate that has already been visited.

Therefore, it doesn't scale the complexity in polynomial time, it just basically adds another O(m x n) complexity in the worse case (furthest recursive depth, all 1s), meaning the complexity is 2O(m x n), but we can ignore the scalar, as we did the other O(m x n) traversals in the error checking segment, resulting in O(m x n).

Alternatively, the best case scenarion would be a matrix of all 0s, but it is still going to be O(m x n) overall. We'll touch all the items (m x n) in the main loop, but never encouter a 1 and thereofore never do any recursive work.

An all "0" matrix would be marginally faster, but best and worse case all scale in O(m x n) time still.

### Depth First or Breadth First?
I have an algorithm to count "islands" of 1's in matrices of only 1s and 0s. It uses a recursive function that is called from a loop to touch every item in row major order.

In the main loop, we check if an item is a 1 and if it has not yet been visited. If these 2 conditions are true, the recursive function is called on that "coordinate". It in turn either returns if the coordinate is any of the following:
1. A 0
2. Already visited (tracked in a "visited" memoization)
3. Out of the matrix bounds
...or it marks the item as visited, then calls itself on its 4 direct neighbors.

every time the main loop finds a new item that is an unvisited "1", a counter is incremented. At the end, this is the number of "islands"

This algorithm implements depth-first traversal (DFS).
The defining characteristic is that the recursive function calls itself on the 4 neighbors before returning. When an unvisited "1" is encountered, the algorithm immediately explores that entire island by following one path as far as possible through recursive calls before backtracking to explore alternative paths.
The traversal pattern follows this sequence:

Locate unvisited "1" → invoke recursive function
Recursive function marks current cell as visited
Immediately calls itself on first neighbor (proceeding deeper)
That call proceeds even deeper on its first unvisited neighbor
This continues until reaching a boundary condition (0, visited, or out of bounds)
Only then does backtracking occur to explore the next neighbor

Breadth-first search (BFS) would employ a queue and explore all immediate neighbors before advancing to their neighbors. BFS implementation for this problem would typically follow this pattern:

Locate unvisited "1" → add to queue
While queue is not empty: dequeue a cell, mark as visited, enqueue all unvisited "1" neighbors

The recursive approach naturally utilizes the call stack as the stack data structure that DFS employs, prioritizing depth exploration over breadth exploration.

