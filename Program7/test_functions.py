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

# test with valid matrices
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

# verify invalid matrices are detected
def test_islands_invalid_values():
    matrix : list = [[1, 2, 0],
                     [1, 0, 1],
                     [0, 1, 1],
                     [0, 0, 0]
    ]
    with pytest.raises(ValueError, match="Matrix must consist of 1s and 0s only"):
        islands(matrix)
def test_islands_invalid_ragged():
    matrix : list = [[0, 1, 0],
                     [1, 1]
    ]
    with pytest.raises(ValueError, match="Uneven matrix rows"):
        islands(matrix)
def test_islands_invalid_height():
    matrix : list = [[0] * 5 for item in range(301)]
    with pytest.raises(ValueError, match="Matrix must be 300 \"rows\" or less"):
        islands(matrix)
def test_islands_invalid_width():
    matrix : list = [[0] * 301 for item in range(5)]
    with pytest.raises(ValueError, match="Matrix must be 300 \"columns\" or less"):
        islands(matrix)
