### Program 7

1. Efficiency is:\\
    Fixed O(m x n) (rows x cols) to check if matrix is valid format (1/0 only rectangle)\\
    Fixed O(m x n) again to travel the entire matrix. Checking if items are visited or not.\\
    Variable (max O(m x n)) time to recursively memoize. Only touch each item once,\\
    but has no effect on the previous double for loop.\\
    Some coefficient of O(m x n) overall. Every square needs to be explored.\\
    Not sure it can be optimized much beyond O(m x n) overall complexity.\\
2. Algorithms used were recursive memoization of an identical visited matrix, as well as the concept of depth first search.
