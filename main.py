# assignment1_part1.py

class ListDivideException(Exception):
    pass

def list_divide(numbers, divide=2):
    try:
        count = sum(1 for num in numbers if num % divide == 0)
        return count
    except ZeroDivisionError:
        raise ListDivideException("Cannot divide by zero")

def test_list_divide():
    try:
        assert list_divide([1, 2, 3, 4, 5]) == 2
        assert list_divide([2, 4, 6, 8, 10]) == 5
        assert list_divide([30, 54, 63, 98, 100], divide=10) == 2
        assert list_divide([1, 2, 3, 4, 5], 1) == 5
    except AssertionError:
        raise ListDivideException("Test failed")

# Run the test
test_list_divide()

# Uncomment the following lines when you have set up your GitHub repository
# import subprocess
# subprocess.run(["git", "add", "assignment1_part1.py"])
# subprocess.run(["git", "commit", "-m", "Add assignment1_part1.py"])
# subprocess.run(["git", "push", "origin", "master"])
