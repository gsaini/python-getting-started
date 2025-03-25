import pytest
from src.problem_solving_questions.plus_one import plus_one

def test_plus_one():
    """
    Test the plus_one function with various test scenarios.
    """
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plus_one([0]) == [1]
    assert plus_one([9]) == [1, 0]

if __name__ == '__main__':
    pytest.main()