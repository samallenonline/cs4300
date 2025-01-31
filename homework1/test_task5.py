# objective: test the task5.py program using pytest

# import appropriate functions to be tested
import subprocess

# test first part of task 5- printing the first 3 items in my_favorite_albums list
def test_favorite_albums():
    result = subprocess.run(["python3", "task5.py"], capture_output=True, text=True)
    assert result.stdout == "['E - Ecco2k', 'Slide - George Clanton', 'Warlord - Yung Lean']\n"

# test seconfd part of task 5