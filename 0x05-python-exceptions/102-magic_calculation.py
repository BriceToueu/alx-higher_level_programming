#!/usr/bin/python3
# 102-magic_calculation.py
# Brice Toueu

def magic_calculation(a, b):
    """
    Performs a calculation based on the given arguments a and b.

    Args:
        a (int): The first parameter, used in the calculation and comparison.
        b (int): The second parameter,
        used in the calculation and as a fallback result.

    Returns:
        float: The result of the calculation,
        which is either a ** b / i or b + a.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += ((a ** b) / i)
        except:
            result = (b + a)
            break
    return (result)
