# Source: https://leetcode.com/problems/plus-one/
def plus_one(digits):
    """
    Given a list of digits representing a non-negative integer, increment the integer by one and return the resulting list of digits.
    
    Args:
    digits (List[int]): A list of digits representing a non-negative integer.
    
    Returns:
    List[int]: The resulting list of digits after incrementing the integer by one.
    
    Example:
    plus_one([1, 2, 3]) -> [1, 2, 4]
    plus_one([9, 9, 9]) -> [1, 0, 0, 0]
    
    The function works by iterating through the list of digits from the end to the beginning.
    If a digit is 9, it is set to 0 and the loop continues to the next digit.
    If a digit is not 9, it is incremented by 1 and the function returns the modified list.
    If all digits are 9, a 1 is inserted at the beginning of the list.
    """
    n = len(digits)

    for i in range(n-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    
    digits.insert(0, 1)
    return digits