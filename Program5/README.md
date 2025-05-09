To use the pytest suite for this program, create a venv and then run:
`pip install -r requirements.txt`

 Solution to find if an item is present in a matrix of at most 100
   1. Target cannot be greater than 100000
   2. Values in the matrix cannot be less than 0.001
   3. Matrix must have a height of at least 1
   4. Rows must contain at most 100 items
   5. Solution must run w/ O(log(m x n)) complexity

 To achieve logarithmic complexity, where the n is the number of items in the "area" of the square matrix, we'll use interval halving and recursion
 First, find a midpoint in the rows and determine if the target is:
   1. in that row
   2. in the rows above
   3. in the rows below

 At each recursive call, we'll bisect the matrix rows and enter a new frame w/ a smaller matrix (the rows above or below the midpoint)
 Alternatively, if the target is found to be in the row of the midpoint, or if the smaller matrix consists of only 1 row, a new recursive binary search function can be called.
 This function will operate similary, but on a single list, the desired row passes as a parameter from the initial function.
 Because we recurse on the height first, using a binary search pattern we traverse all the values in the height (m) in logarithmic time.
 Then, We'll eventually recurse on a single row of "n" items applying the same binary search logic, again resulting in logarithmic time.
 However, the find_row function will only be called once, not on every row.
