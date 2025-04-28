import pytest
from min_sum import min_sum_naiive, min_sum_memo, min_sum_tab

####################################################################
# Ian Leuty & Stephen Feng
# ileuty@pdx.edu
# 4/24/2025
# CS350 Spring 2025
# Homework 4
#####################################################################
# test suite for the 3 minimum descent methods as well as erroneous cases
#####################################################################

# test memo and tab on "same seeded" fixture for verification
@pytest.mark.timeout(10)
def test_min_sum_memo_vs_tab_large_random_tringle(large_random_triangle):
    assert (min_sum_tab(large_random_triangle) == min_sum_memo(large_random_triangle))

#####################################################################

##################### NAIIVE SOLUTION TESTS #########################

# benchmarking tests
# 5 sufficiently large sets - timeout if not calcualted in 10s
@pytest.mark.timeout(10)
def test_min_sum_naiive_large_regular(large_regular_triangle, benchmark):
    result : int = benchmark(min_sum_naiive, large_regular_triangle)
    assert (result == 190)
@pytest.mark.timeout(10)
def test_min_sum_naiive_large_random_triangle(large_random_triangle, benchmark):
    result : int = benchmark(min_sum_naiive, large_random_triangle)
    assert (result == 755)
@pytest.mark.timeout(10)
def test_min_sum_naiive_worst_case_triangle(worst_case_triangle, benchmark):
    result : int = benchmark(min_sum_naiive, worst_case_triangle)
    assert (result == 129)
@pytest.mark.timeout(10)
def test_min_sum_naiive_exponential_triangle(exponential_triangle, benchmark):
    result : int = benchmark(min_sum_naiive, exponential_triangle)
    assert (result > 200 and result < 204)
@pytest.mark.timeout(10)
def test_min_sum_naiive_fibonacci_triangle(fibonacci_triangle, benchmark):
    result : int = benchmark(min_sum_naiive, fibonacci_triangle)
    assert (result == 25)

#standard test cases
@pytest.mark.parametrize("matrix, result", [
    ([[2], [5, 4], [1, 4, 7], [8, 6, 9, 6]], 14),
    ([[4], [4, 4], [4, 4, 4], [4, 4, 4, 4]], 16),
    ([[6], [2, 1], [4, 1, 1], [1, 10, 9, 6]], 13),
    ([[3], [2, 4], [7, 2, 1], [4, 10, 1, 6]], 8),
        # Basic triangle:
        #    2
        #   5 4
        #  1 4 7
    ([[2], [5, 4], [1, 4, 7]], 8),  # 2->5->1
        # Larger triangle:
        #     3
        #    7 4
        #   2 4 6
        #  8 5 9 3
    ([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]], 16),  # 3->4->2->5
        # Triangle with negative values:
        #     -1
        #    2 -3
        #   1 -2 3
    ([[-1], [2, -3], [1, -2, 3]], -6),  # -1->-3->-2
        # Triangle with zeros:
        #     0
        #    0 0
        #   0 0 0
    ([[0], [0, 0], [0, 0, 0]], 0),
        # Single value triangle
    ([[5]], 5),
        # Two rows triangle:
        #    1
        #   2 3
    ([[1], [2, 3]], 3), # 1 -> 2
        #    10
        #   1 15
        #  1 30 5
    ([[10], [1, 15], [1, 30, 5]], 12),
        # Complex triangle:
        #     7
        #    3 8
        #   8 1 0
        #  2 7 4 4
        # 9 6 2 1 7
    ([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [9, 6, 2, 1, 7]], 16), # 7->3->1->4->1
        # Another trap case:
        #     8
        #    2 4
        #   3 1 9
        #  5 6 4 7
    ([[8], [2, 4], [3, 1, 9], [5, 6, 4, 7]], 15), # 8->2->1->4
        # Descending values:
        #    100
        #   99 98
        #  97 96 95
    ([[100], [99, 98], [97, 96, 95]], 293), # 100->98->95
        # Increasing orders of magnitude:
        #      1
        #    10 20
        #  100 200 300
        # 1000 2000 3000 4000
    ([[1], [10, 20], [100, 200, 300], [1000, 2000, 3000, 4000]], 1111), # 1->10->100->1000
        # Zigzag minimum path:
        #     5
        #    4 1
        #   3 10 4
        #  8 2 3 1
        # 9 4 5 7 2
    ([[5], [4, 1], [3, 10, 4], [8, 2, 3, 1], [9, 4, 5, 7, 2]], 13)# 5->1->3->1->2
    ])
def test_min_sum_naiive(matrix, result):
    actual_result : int = min_sum_naiive(matrix)
    assert(actual_result == result)

# erroneous inputs
def test_min_sum_naiive_empty():
    with pytest.raises(ValueError, match="Empty matrix"):
        min_sum_naiive([])
    with pytest.raises(ValueError, match="Empty row present. Cannot find min descent"):
        min_sum_naiive([[], [], []])
    with pytest.raises(ValueError, match="Empty row present. Cannot find min descent"):
        min_sum_naiive([[1], [], [2, 4, 5]])
    with pytest.raises(ValueError, match="Empty row present. Cannot find min descent"):
        min_sum_naiive([[], [2], [4, 5]])

#####################################################################

################### MEMOIZED SOLUTION TESTS #########################

# benchmarking tests
# 5 sufficiently large sets - timeout if not calcualted in 10s
@pytest.mark.timeout(10)
def test_min_sum_memo_large_regular(large_regular_triangle, benchmark):
    result : int = benchmark(min_sum_memo, large_regular_triangle)
    assert (result == 190)
@pytest.mark.timeout(10)
def test_min_sum_memo_worst_case_triangle(worst_case_triangle, benchmark):
    result : int = benchmark(min_sum_memo, worst_case_triangle)
    assert (result == 129)
# don't care about random result, just timing a benchmark
@pytest.mark.timeout(10)
def test_min_sum_memo_large_random_triangle(large_random_triangle, benchmark):
    result2 : int = (benchmark(min_sum_memo, large_random_triangle))
@pytest.mark.timeout(10)
def test_min_sum_memo_exponential_triangle(exponential_triangle, benchmark):
    result : int = benchmark(min_sum_memo, exponential_triangle)
    assert (result > 200 and result < 204)
@pytest.mark.timeout(10)
def test_min_sum_memo_fibonacci_triangle(fibonacci_triangle, benchmark):
    result : int = benchmark(min_sum_memo, fibonacci_triangle)
    assert (result == 25)

# standard test cases
@pytest.mark.parametrize("matrix, result", [
    ([[2], [5, 4], [1, 4, 7], [8, 6, 9, 6]], 14),
    ([[4], [4, 4], [4, 4, 4], [4, 4, 4, 4]], 16),
    ([[6], [2, 1], [4, 1, 1], [1, 10, 9, 6]], 13),
    ([[3], [2, 4], [7, 2, 1], [4, 10, 1, 6]], 8),
        # Basic triangle:
        #    2
        #   5 4
        #  1 4 7
    ([[2], [5, 4], [1, 4, 7]], 8),  # 2->5->1
        # Larger triangle:
        #     3
        #    7 4
        #   2 4 6
        #  8 5 9 3
    ([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]], 16),  # 3->4->2->5
        # Triangle with negative values:
        #     -1
        #    2 -3
        #   1 -2 3
    ([[-1], [2, -3], [1, -2, 3]], -6),  # -1->-3->-2
        # Triangle with zeros:
        #     0
        #    0 0
        #   0 0 0
    ([[0], [0, 0], [0, 0, 0]], 0),
        # Single value triangle
    ([[5]], 5),
        # Two rows triangle:
        #    1
        #   2 3
    ([[1], [2, 3]], 3), # 1 -> 2
        #    10
        #   1 15
        #  1 30 5
    ([[10], [1, 15], [1, 30, 5]], 12),
        # Complex triangle:
        #     7
        #    3 8
        #   8 1 0
        #  2 7 4 4
        # 9 6 2 1 7
    ([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [9, 6, 2, 1, 7]], 16), # 7->3->1->4->1
        # Another trap case:
        #     8
        #    2 4
        #   3 1 9
        #  5 6 4 7
    ([[8], [2, 4], [3, 1, 9], [5, 6, 4, 7]], 15), # 8->2->1->4
        # Descending values:
        #    100
        #   99 98
        #  97 96 95
    ([[100], [99, 98], [97, 96, 95]], 293), # 100->98->95
        # Increasing orders of magnitude:
        #      1
        #    10 20
        #  100 200 300
        # 1000 2000 3000 4000
    ([[1], [10, 20], [100, 200, 300], [1000, 2000, 3000, 4000]], 1111), # 1->10->100->1000
        # Zigzag minimum path:
        #     5
        #    4 1
        #   3 10 4
        #  8 2 3 1
        # 9 4 5 7 2
    ([[5], [4, 1], [3, 10, 4], [8, 2, 3, 1], [9, 4, 5, 7, 2]], 13)# 5->1->3->1->2
    ])
def test_min_sum_memo(matrix, result):
    actual_result : int = min_sum_memo(matrix)
    assert(actual_result == result)

# erroneous inputs
def test_min_sum_memo_empty():
    with pytest.raises(ValueError, match="Empty matrix"):
        min_sum_memo([])
    with pytest.raises(ValueError, match="Empty row present. Cannot find min descent"):
        min_sum_memo([[], [], []])
    with pytest.raises(ValueError, match="Empty row present. Cannot find min descent"):
        min_sum_memo([[1], [], [2, 4, 5]])
    with pytest.raises(ValueError, match="Empty row present. Cannot find min descent"):
        min_sum_memo([[], [2], [4, 5]])

#####################################################################

################## TABULATION SOLUTION TESTS ########################

# benchmarking tests
# 5 sufficiently large sets - timeout if not calcualted in 10s
@pytest.mark.timeout(10)
def test_min_sum_tab_large_regular(large_regular_triangle, benchmark):
    result : int = benchmark(min_sum_tab, large_regular_triangle)
    assert (result == 190)
@pytest.mark.timeout(10)
def test_min_sum_tab_worst_case_triangle(worst_case_triangle, benchmark):
    result : int = benchmark(min_sum_tab, worst_case_triangle)
    assert (result == 129)
# don't care about random result - just benchmarking
@pytest.mark.timeout(10)
def test_min_sum_tab_large_random_triangle(large_random_triangle, benchmark):
    result : int = benchmark(min_sum_tab, large_random_triangle)
@pytest.mark.timeout(10)
def test_min_sum_tab_exponential_triangle(exponential_triangle, benchmark):
    result : int = benchmark(min_sum_tab, exponential_triangle)
    assert (result > 200 and result < 204)
@pytest.mark.timeout(10)
def test_min_sum_tab_fibonacci_triangle(fibonacci_triangle, benchmark):
    result : int = benchmark(min_sum_tab, fibonacci_triangle)
    assert (result == 25)

#standard test cases
@pytest.mark.parametrize("matrix, result",  [
    ([[2], [5, 4], [1, 4, 7], [8, 6, 9, 6]], 14),
    ([[4], [4, 4], [4, 4, 4], [4, 4, 4, 4]], 16),
    ([[6], [2, 1], [4, 1, 1], [1, 10, 9, 6]], 13),
    ([[3], [2, 4], [7, 2, 1], [4, 10, 1, 6]], 8),
        # Basic triangle:
        #    2
        #   5 4
        #  1 4 7
    ([[2], [5, 4], [1, 4, 7]], 8),  # 2->5->1
        # Larger triangle:
        #     3
        #    7 4
        #   2 4 6
        #  8 5 9 3
    ([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]], 16),  # 3->4->2->5
        # Triangle with negative values:
        #     -1
        #    2 -3
        #   1 -2 3
    ([[-1], [2, -3], [1, -2, 3]], -6),  # -1->-3->-2
        # Triangle with zeros:
        #     0
        #    0 0
        #   0 0 0
    ([[0], [0, 0], [0, 0, 0]], 0),
        # Single value triangle
    ([[5]], 5),
        # Two rows triangle:
        #    1
        #   2 3
    ([[1], [2, 3]], 3), # 1 -> 2
        #    10
        #   1 15
        #  1 30 5
    ([[10], [1, 15], [1, 30, 5]], 12),
        # Complex triangle:
        #     7
        #    3 8
        #   8 1 0
        #  2 7 4 4
        # 9 6 2 1 7
    ([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [9, 6, 2, 1, 7]], 16), # 7->3->1->4->1
        # Another trap case:
        #     8
        #    2 4
        #   3 1 9
        #  5 6 4 7
    ([[8], [2, 4], [3, 1, 9], [5, 6, 4, 7]], 15), # 8->2->1->4
        # Descending values:
        #    100
        #   99 98
        #  97 96 95
    ([[100], [99, 98], [97, 96, 95]], 293), # 100->98->95
        # Increasing orders of magnitude:
        #      1
        #    10 20
        #  100 200 300
        # 1000 2000 3000 4000
    ([[1], [10, 20], [100, 200, 300], [1000, 2000, 3000, 4000]], 1111), # 1->10->100->1000
        # Zigzag minimum path:
        #     5
        #    4 1
        #   3 10 4
        #  8 2 3 1
        # 9 4 5 7 2
    ([[5], [4, 1], [3, 10, 4], [8, 2, 3, 1], [9, 4, 5, 7, 2]], 13)# 5->1->3->1->2
    ])
def test_min_sum_tab(matrix, result):
    actual_result : int = min_sum_tab(matrix)
    assert(actual_result == result)

#erroneous inputs
def test_min_sum_tab_empty():
    with pytest.raises(ValueError, match="Empty matrix"):
        min_sum_tab([])
    with pytest.raises(ValueError, match="Empty row present. Cannot find min descent"):
        min_sum_tab([[], [], []])
    with pytest.raises(ValueError, match="Empty row present. Cannot find min descent"):
        min_sum_tab([[1], [], [2, 4, 5]])
    with pytest.raises(ValueError, match="Empty row present. Cannot find min descent"):
        min_sum_tab([[], [2], [4, 5]])

#####################################################################
