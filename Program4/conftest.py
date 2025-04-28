import pytest
import random

####################################################################
# Ian Leuty & Stephen Feng
# ileuty@pdx.edu
# 4/24/2025
# CS350 Spring 2025
# Homework 4
#####################################################################
# pytest fixures for benchmarking - complicated and sufficiently large triangle matrices to demonstrate efficiency of memoization
#####################################################################

# set random seed for reproducibility
random.seed(42)

# test case 1: Large regular triangle (20 rows)
# j pattern where values increase by position
'''
0
1 2
2 3 4
3 4 5 6
4 5 6 7 8
...and so on until row 20
'''
@pytest.fixture
def large_regular_triangle() -> list:
    large_regular_triangle = []
    for i in range(20):
        row = []
        for j in range(i+1):
            row.append(i+j)
        large_regular_triangle.append(row)
    return large_regular_triangle

# test case 2: large random triangle (25 rows)
'''
63
91 21
5 10 54
...and so on for 25 rows
'''
@pytest.fixture
def large_random_triangle() -> list:
    large_random_triangle = []
    for i in range(25):
        large_random_triangle.append([random.randint(1, 100) for _ in range(i+1)])
    return large_random_triangle

# test case 3: worst-case for naive approach (30 rows)
# a triangle where the minimum path zigzags
'''
100
100 100
100 1 100
100 100 100 100
100 1 100 100 100
...continues with 1 in middle position...
After row 15, the middle values (which were initially attractive at 1) become bad (200), and the path shifts left:
100 100 1 100 ... 100
100 1 200 100 ... 100
1 100 200 100 ... 100
...continues with best path zigzagging left...
'''
@pytest.fixture
def worst_case_triangle() -> list:
    worst_case_triangle = []
    for i in range(30):
        row = []
        for j in range(i+1):
            if j == i//2:  # make the middle path initially attractive
                row.append(1)
            else:
                row.append(100)
        worst_case_triangle.append(row)
# then add a twist at the end to force recalculation
    for i in range(15, 30):
        j = i//2  # the middle position
        worst_case_triangle[i][j] = 200  # make the middle bad
        if j > 0:
            worst_case_triangle[i][j-1] = 1  # make left path good
    return worst_case_triangle

# test case 4: exponential complexity trigger (20 rows)
# this creates many equally viable paths that need to be explored
'''
10.4
10.2 10.5
10.3 10.1 10.5
...and so on for 20 rows
'''
@pytest.fixture
def exponential_triangle():
    exponential_triangle = []
    for i in range(20):
        row = []
        for j in range(i+1):
            # all values are close to 10, with small random variations
            row.append(10 + random.randint(0, 5) / 10.0)
        exponential_triangle.append(row)
    return exponential_triangle

# test case 5: fibonacci-like growth test (25 rows)
# values arranged to create many overlapping subproblems
'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
...
Similar to Pascal's triangle but with a max function applied to ensure values grow in a Fibonacci-like pattern.
'''
@pytest.fixture
def fibonacci_triangle() -> list:
    fibonacci_triangle = [[1]]
    for i in range(1, 25):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)  # Edge values are 1
            else:
                # middle values follow fibonacci-like pattern
                row.append(max(1, fibonacci_triangle[i-1][max(0,j-1)] +
                              fibonacci_triangle[i-1][min(j,i-1)]))
        fibonacci_triangle.append(row)
    return fibonacci_triangle
