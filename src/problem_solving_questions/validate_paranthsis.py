def validate_paranthsis(str):

    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    
    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    
    The function uses a stack to keep track of the opening brackets. When an opening bracket is encountered, it is pushed onto the stack.
    When a closing bracket is encountered, the function checks if it matches the top of the stack (i.e., the most recent unmatched opening bracket).
    If it matches, the opening bracket is popped from the stack. If it does not match, the function returns False immediately.
    After processing all characters in the string, the stack should be empty if all opening brackets have been matched correctly.
    
    Parameters:
    str (str): The input string containing the brackets to be validated.
    
    Returns:
    bool: True if the input string is valid, False otherwise.
    
    """
    stack = []
    paranthsis = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for i in str:
        if i in paranthsis:
            stack.append(i)
        else:
            if not stack or paranthsis[stack.pop()] != i:
                return False
        
    return not stack
