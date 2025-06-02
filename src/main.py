def happy_number(num):
    """
    Determines whether a given number is a happy number.

    A happy number is defined by the following process:
    1. Starting with any positive integer, replace the number by the sum of the squares of its digits
    2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly

    Args:
        num (int): A positive integer to check

    Returns:
        bool: True if the number is happy, False if it's not

    Examples:
        >>> happy_number(19)
        True  # 1² + 9² = 82, 8² + 2² = 68, 6² + 8² = 100, 1² + 0² + 0² = 1
        >>> happy_number(4)
        False  # 4² = 16, 1² + 6² = 37, 3² + 7² = 58, 5² + 8² = 89, 8² + 9² = 145, ...
    """
    seen_nums = set()
    while num != 1 and num not in seen_nums:
        seen_nums.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1