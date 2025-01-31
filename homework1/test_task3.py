# objective: test the task3.py program using pytest

# import appropriate functions to be tested
from task3 import positive_or_negative, sum_of_numbers, first_10_prime

# test the output of each function 
def test_demonstrate_control_structures():
     assert positive_or_negative(5) == ("Positive")
     assert positive_or_negative(0) == ("Zero")
     assert positive_or_negative(-5) == ("Negative")

     assert first_10_prime() == ([1, 2, 3, 5, 7, 11, 13, 17, 19, 23])

     assert sum_of_numbers() == (5050)