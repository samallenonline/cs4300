# objective: test the task1.py program using pytest

# import appropriate function to be tested
from task1 import hello_world

# test output of function
def test_hello_world_output():
    assert hello_world() == "Hello, World!"