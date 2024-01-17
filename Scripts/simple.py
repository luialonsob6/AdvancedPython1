"""
Scripts to write sum and substract functions
"""
import math


def sum_two_nums(x, y):
    """
    Sum two nums
    """

    return x + y


def sub_two_nums(x, y):
    """
    Substract two numbers
    """

    return x - y


def divide_two_numbers(x, y):
    """
    Divide two numbers
    """
    return x / y


def lcm_two_numbers(x, y):
    """
    Search the least common multiple
    """
    gcd = math.gcd(x, y)
    lcm = abs(x * y) // gcd
    return lcm


def potency_two_numbers(x, y):
    """
    Calculate the result of x elevated to y
    """
    return x**y


if __name__ == "__main__":
    pass
