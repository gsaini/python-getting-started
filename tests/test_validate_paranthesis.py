import pytest

from src.problem_solving_questions.validate_paranthsis import validate_paranthsis

def test_validate_paranthsis():
    """
    Test case 1:
    str = "()" -> True
    The input string contains a pair of matching brackets, so it is valid.  
    """ 
    assert validate_paranthsis("()") == True

    """
    Test case 2:
    str = "()[]{}" -> True
    The input string contains multiple pairs of matching brackets, so it is valid.
    """ 
    assert validate_paranthsis("()[]{}") == True

    """
    Test case 3:
    str = "(]" -> False
    The input string contains a pair of brackets that do not match, so it is invalid.
    """ 
    assert validate_paranthsis("(]") == False

    """
    Test case 4:
    str = "([)]" -> False
    The input string contains a pair of brackets that do not match, so it is invalid.
    """ 
    assert validate_paranthsis("([)]") == False

    """
    Test case 5:
    str = "{[]}" -> True
    The input string contains multiple pairs of matching brackets, so it is valid.
    """ 
    assert validate_paranthsis("{[]}") == True

    """
    Test case 6:
    str = "[" -> False
    The input string contains an unmatched opening bracket, so it is invalid.
    """ 
    assert validate_paranthsis("[") == False

    """
    Test case 7:
    str = "]" -> False
    The input string contains an unmatched closing bracket, so it is invalid.
    """ 
    assert validate_paranthsis("]") == False

    """
    Test case 8:
    str = "([{}])" -> True
    The input string contains multiple pairs of matching brackets, so it is valid.
    """ 
    assert validate_paranthsis("([{}])") == True