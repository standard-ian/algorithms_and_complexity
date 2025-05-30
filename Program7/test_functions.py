####################################################################
# Ian Leuty
# ileuty@pdx.edu
# 5/27/2025
# CS350 Spring 2025
# Homework 7
#####################################################################
# test suite for the islands function
#####################################################################

import pytest
from functions import islands

@pytest.mark.parametrize("matrix, result", [
    ([[1, 1, 1, 1, 0],
      [1, 1, 0, 1, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0]
     ], 1),

    ([[1, 1, 0, 0, 0],
      [1, 1 ,0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 1, 1]
     ], 3),

    ([[1, 1, 0, 1],
      [1, 1, 0, 1],
      [1, 1, 0, 0],
      [0, 0, 0, 0]
    ], 2),

    ([[1, 1, 1, 1, 0],
      [1, 1, 0, 1, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [1, 0, 1, 1, 1],
      [0, 0, 0, 0, 1],
      [1, 0, 0, 0, 1]
    ], 4),

    ([[0, 0],
      [0, 0],
      [1, 1],
      [0, 0]
    ], 1),

    ([[1, 0, 0, 1, 0, 0],
      [1, 0, 0, 1, 0, 1],
      [1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0],
      [1, 0, 0, 0 ,0, 1],
      [1, 1, 0, 0, 0, 1]
    ], 6),

    ])
def test_islands(matrix, result):
    assert (islands(matrix) == result)

def test_islands_invalid():
    matrix : list = [[1, 2, 0],
                     [1, 0, 1],
                     [0, 1, 1],
                     [0, 0, 0]
                    ]
    with pytest.raises(ValueError, match="Matrix must consist of 1s and 0s only"):
        islands(matrix)
    matrix : list = [[0, 1, 0],
                     [1, 1]
                    ]
    with pytest.raises(ValueError, match="Uneven matrix rows"):
        islands(matrix)


