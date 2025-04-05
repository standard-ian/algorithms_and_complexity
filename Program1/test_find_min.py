import find_min
import pytest

@pytest.mark.parametrize("test_list, actual_min", [
    ([3, 4, 5, 6, -1, 2], -1),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
    ([5, 6, 7, 8, 9, 10, 1, 2, 3, 4], 1),
    ([0, 1, 2, 4, 5, 6, 7], 0),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([30, 40, 50, 66, 78, 11, 24], 11),
    ([6, 7, 1, 2, 3, 4, 5], 1),
    ([-3, -2, -1, 0, 1, 2], -3),
    ([-5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000], -5000),
    ([1],1)
])
def test_find_min(test_list, actual_min):
    assert find_min.find_minimum(test_list) == actual_min

