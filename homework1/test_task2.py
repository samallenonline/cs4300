# objective: test the task2.py program using pytest

# import appropriate functions to be tested
from task2 import demonstrate_ints, demonstrate_floats, demonstrate_strings, demonstrate_bools

# test the output of each function 
def test_demonstrate_data_types():
    assert demonstrate_ints() == (4, 0, 21)
    assert demonstrate_floats() == (5.0, 1.0, 25.2)
    assert demonstrate_strings() == ('Hi there', 'HI THERE', 'H')
    assert demonstrate_bools() == (True, False, True)
