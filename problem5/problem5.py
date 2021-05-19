"""
PROBLEM #5 [MEDIUM]

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    """
    given a function f
    define how to return the first element given a pair
    and return the left() applied to that function
    """
    def left(a, b):
        return a
    return f(left)

def cdr(f):
    """
    given a function f
    define how to return the last element given a pair
    and return the right() applied to that function
    """
    def right(a, b):
        return b
    return f(right)


if __name__ == "__main__":
    # key concept here is to think with a functional programming mindset
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4
    print("Successfully tested.")
