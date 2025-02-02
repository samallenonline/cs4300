# objective: test the task5.py program using pytest

# import appropriate functions to be tested
from task5 import get_top_three_albums, get_student_info

# test the output of each function 
def test_get_top_three_albums():
    assert get_top_three_albums() == ['E - Ecco2k', 'Slide - George Clanton', 'Warlord - Yung Lean']

def test_get_student_info():
    assert get_student_info() == ({'Name': 'Sam Allen', 'ID': '110782875'}, 'Sam Allen', '110782875')