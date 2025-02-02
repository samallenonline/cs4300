# objective: test the task7.py program using pytest

# import appropriate packages and functions to be tested
from task7 import matrix_multiplication
import numpy as np

# test the output of each function 
def test_matrix_multiplication():
    expected_result = np.array([[19, 22], [43, 50]])  
    actual_result = matrix_multiplication()

    # must use np.testing to compare the numpy data structures for effective testing 
    np.testing.assert_array_equal(actual_result, expected_result)