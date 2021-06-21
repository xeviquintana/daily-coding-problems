"""
PROBLEM 12 [HARD]

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

def climb(N: int) -> int:
    """
    Key point is to detect this is a fibo series
    If there's just 1 step      climb(1) = 1
    If there are 2 steps        climb(2) = 2
    If there are 3 steps        climb(3) = climb(2) + climb(1)
    If there are 4 steps        climb(4) = climb(3) + climb(2)
    """
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return climb(N-1) + climb(N-2)

def climb_flex(N: int, X: [int]) -> int:
    """
    The key here is to think of N as the root of a tree with len(X) childs
    Each x in {X} is a subtree having its root value N-x
    Process each subtree until root value is 0 (success path) or <0 (failure).
    """
    if N < 0:
        return 0
    elif N == 0:
        return 1
    else:
        res = 0
        for step in X:
            if N-step >= 0: # just to avoid unnecessary recursion calls
                res += climb_flex(N-step, X)
    return res


if __name__ == "__main__":
    assert climb(0) == 0
    assert climb(1) == 1
    assert climb(2) == 2
    assert climb(3) == 3
    assert climb(4) == 5
    assert climb(5) == 8
    assert climb(6) == 13

    assert climb_flex(2, [2]) == 1
    assert climb_flex(3, [1, 2]) == 3
    assert climb_flex(6, [1, 2]) == 13
    assert climb_flex(3, [1, 3]) == 2
    assert climb_flex(5, [1, 3, 4]) == 6

    print("Successfully tested.")
