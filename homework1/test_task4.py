# objective: test the task4.py program using pytest

# import appropriate functions to be tested
from task4 import calculate_discount

# test the output of each function 
def test_calculate_discount():
    assert calculate_discount(50.49, 25) == (37.87)
    assert calculate_discount(50, 25.50) == (37.25)
    assert calculate_discount(50, 25) == (37.5)
    assert calculate_discount(19.99, 15.50) == (16.89)