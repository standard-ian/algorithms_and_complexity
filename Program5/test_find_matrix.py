import pytest
from find_matrix import find

####################################################################
# Ian Leuty
# ileuty@pdx.edu
# 5/9/2025
# CS350 Spring 2025
# Homework 5
#####################################################################
# Pytest suite for find function (find if a value is in a matrix and return a boolean)
#####################################################################
#
@pytest.mark.parametrize("matrix, target, is_present", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 7, True),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 23, False),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, True),
    ([[99, 104, 392, 503, 820, 999], [1034, 1088, 1500, 2005, 2693, 4000], [5000, 5032, 5999, 6000, 6001, 6002]], 6001, True),
    ([[99, 104, 392, 503, 820, 999], [1034, 1088, 1500, 2005, 2693, 4000], [5000, 5032, 5999, 6000, 6001, 6002]], 5000, True),
    ([[99, 104, 392, 503, 820, 999], [1034, 1088, 1500, 2005, 2693, 4000], [5000, 5032, 5999, 6000, 6001, 6002]], 99, True),
    ([[99, 104, 392, 503, 820, 999], [1034, 1088, 1500, 2005, 2693, 4000], [5000, 5032, 5999, 6000, 6001, 6002]], 820, True),
    ([[99, 104, 392, 503, 820, 999], [1034, 1088, 1500, 2005, 2693, 4000], [5000, 5032, 5999, 6000, 6001, 6002]], 7000, False),
    ([[99, 104, 392, 503, 820, 999], [1034, 1088, 1500, 2005, 2693, 4000], [5000, 5032, 5999, 6000, 6001, 6002]], 3400, False)
    ])
def test_find(matrix, target, is_present):
    assert (find(matrix, target) == is_present)


def test_invalid_find():
    # ensure invalid minimum value raises error
    with pytest.raises(ValueError, match="Invalid matrix: min value is less than one ten-thousandth"):
        find([[0.0001, 104, 392, 503, 820, 999], [1034, 1088, 1500, 2005, 2693, 4000], [5000, 5032, 5999, 6000, 6001, 6002]], 6001)

    # ensure invalid target raises error
    with pytest.raises(ValueError, match="Invalid target: must equivalent to 100,000 or less"):
        find([[99, 104, 392, 503, 820, 999], [1034, 1088, 1500, 2005, 2693, 4000], [5000, 5032, 5999, 6000, 6001, 6002]], 1000000)

    # ensure empty matrix, or empty row raises error
    with pytest.raises(ValueError, match="Invalid matrix: Cannot be empty"):
        find([], 9)
        find([[], [], []], 9)
        find([[1, 2, 4], [], [10, 11, 12]], 9)

    # build a matrix w/ invalid number of rows
    long_one = []
    for i in range(200):
        long_one.append([10])
    # ensure a too-long matrix raises error
    with pytest.raises(ValueError, match="Invalid matrix: greater than 100 rows"):
        find(long_one, 23)
