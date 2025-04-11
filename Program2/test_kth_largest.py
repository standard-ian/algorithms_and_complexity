####################################################################
# Ian Leuty
# ileuty@pdx.edu
# 4/10/2025
# CS350 Spring 2025
# Homework 2
#####################################################################
# pytest suite for k-th largest finding function
#####################################################################
#

import pytest
from kth import kth_largest

# test different k values from different scrambled lists, duplicates, negatives
@pytest.mark.parametrize("the_list, k, k_val", [
    ([2, 3, 1, 0, 4], 1, 4),
    ([2, 5, 4, 1, 0, 3], 2, 4),
    ([2, 5, 4, 1, 0, 3], 1, 5),
    ([2, 5, 4, 1, 0, 3], 5, 1),
    ([2, 5, 4, 1, 0, 3], 6, 0),
    ([2, 3, 5, 6, 0, 1], 1, 6),
    ([2, 3, 5, 6, 0, 1], 2, 5),
    ([9, 7, 5, 11, 12, 2], 1, 12),
    ([9, 7, 5, 11, 12, 2], 6, 2),
    ([4, 2, 9, 7, 5, 6, 1], 4, 5),
    ([4, 2, 9, 7, 5, 6, 1], 1, 9),
    ([4, 2, 9, 7, 5, 6, 1], 7, 1),
    ([15, 3, 9, 8, 2, 1, 4, 10], 2, 10),
    ([15, 3, 9, 8, 2, 1, 4, 10], 3, 9),
    ([15, 3, 9, 8, 2, 1, 4, 10], 8, 1),
    ([20, 19, 18, 17, 16], 1, 20),
    ([20, 19, 18, 17, 16], 3, 18),
    ([20, 19, 18, 17, 16], 5, 16),
    ([1, 2, 3, 4, 5], 1, 5),
    ([1, 2, 3, 4, 5], 3, 3),
    ([1, 2, 3, 4, 5], 5, 1),
    ([10], 1, 10),
    ([5, 5, 5, 5, 5], 1, 5),
    ([5, 5, 5, 5, 5], 3, 5),
    ([5, 5, 5, 5, 5], 5, 5),
    ([3, 1, 4, 1, 5, 9, 2, 6], 5, 3),
    ([3, 1, 4, 1, 5, 9, 2, 6], 1, 9),
    ([3, 1, 4, 1, 5, 9, 2, 6], 8, 1),
    ([100, 42, 17, 13, 28], 3, 28),
    ([2, 3, 1, 0, 4], 1, 4),
    ([2, 5, 4, 1, 0, 3], 2, 4),
    ([2, 5, 4, 1, 0, 3], 1, 5),
    ([2, 5, 4, 1, 0, 3], 5, 1),
    ([2, 5, 4, 1, 0, 3], 6, 0),
    ([2, 3, 5, 6, 0, 1], 1, 6),
    ([2, 3, 5, 6, 0, 1], 2, 5),
    ([3, 1, 6, 4, 7], 1, 7),
    ([2, 5, 2, 7, 1, 3], 4, 2),
    ([3, 1, 6, 4, 7], 4, 3),
    ([5], 1, 5),
    ([-2, 0, 4, 7, 1, -5], 5, -2),
    ([2, 8, 5, 1, 6], 3, 5),
    ([9, 2, 7, 4, 1], 2, 7),
    ([-1, -3, -5, -2, -4], 4, -4),
    ([10, 15, 5, 8, 12], 2, 12)
])
def test_kth_largest(the_list, k, k_val):
    print(f"\nThe array before:  {the_list}")

    result = kth_largest(the_list, k)

    assert (result == k_val)

    print(f"The array after:  {the_list}")
    print(f"k = {k}, k-th largest = {result}")

# test empty arrays
@pytest.mark.parametrize("the_list, k",[
    ([], 1),
    ([], 5)
])
def test_kth_largest_empty(the_list, k):
    with pytest.raises(ValueError, match="Empty list cannot be sorted"):
        kth_largest(the_list, k)

# test invalid k
@pytest.mark.parametrize("the_list, k", [
    ([3, 1, 4, 1, 5, 9, 2, 6], 1000000, 3),
    ([9, 7, 5, 11, 12, 2], 3, 7)
    ])
def kth_largest_invalid_k(the_list, k):
    with pytest.raises(ValueError, match="k out of range"):
        kth_largest(the_list, k)

