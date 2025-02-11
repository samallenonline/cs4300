# objective: test the task2.py program using pytest

# import appropriate functions to be tested
from task2 import demonstrate_ints, demonstrate_floats, demonstrate_strings, demonstrate_bools

# test the type of value returned by each function
def test_demonstrate_data_types():
    assert type(demonstrate_ints()) == int
    assert type(demonstrate_floats()) == float
    assert type(demonstrate_strings()) == str
    assert type(demonstrate_bools()) == bool
