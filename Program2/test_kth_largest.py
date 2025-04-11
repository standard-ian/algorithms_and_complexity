import pytest
from kth import kth_largest

@pytest.mark.parametrize("the_list, k, k_val", [
    ([2, 3, 1, 0, 4], 1, 4),
    ([2, 5, 4, 1, 0, 3], 2, 4),
    ([2, 5, 4, 1, 0, 3], 1, 5),
    ([2, 5, 4, 1, 0, 3], 5, 1),
    ([2, 5, 4, 1, 0, 3], 6, 0),
    ([2, 3, 5, 6, 0, 1], 1, 6),
    #([], 0, 0)
    ([2, 3, 5, 6, 0, 1], 2, 5)
    ])
def test_quicksort(the_list, k, k_val):
    assert kth_largest(the_list, k) == k_val
