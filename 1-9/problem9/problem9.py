"""
# PROBLEM #9 [HARD]

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, `[2, 4, 6, 2, 5]` should return `13`, since we pick `2`, `6`, and `5`. `[5, 1, 1, 5]` should return `10`, since we pick `5` and `5`.

Follow-up: Can you do this in O(N) time and constant space?
"""

def sum_non_adjacent_non_optimal(arr: [int]) -> int:
    """
    Brute-force: check if each element can become part of the solution.
    To do so we compare what's the best:
        exclude current element and consider the others (adjacent), OR
        include current element and consider the others (non adjacent)

    O(n^2) in time
    """

    if not arr:
        return 0
    
    return max(
        sum_non_adjacent_non_optimal(arr[1:]),
        arr[0] + sum_non_adjacent_non_optimal(arr[2:])
    )

def sum_non_adjacent_optimal(arr: [int]) -> int:
    """
    Use dynamic programming to store the larges sum of adjacents for a given position
    Initially used a cache: [int], to store each value of sum_of_adjacents, and
        just return the last position of that. But with constant space we can prevent
        storing all values if we are just interested in the 2 latests positions
    O(n) in time, O(1) in space
    """
    if len(arr) <= 2:
        return max(0, max(arr))

    max_without_last = max(0, arr[0])
    max_with_last = max(max_without_last, arr[1])

    for num in arr[2:]:
        prev_max_with_last = max_with_last

        max_with_last = max(max_with_last, max_without_last + num)
        max_without_last = prev_max_with_last

    return max(max_with_last, max_without_last)


if __name__ == "__main__":
    assert sum_non_adjacent_non_optimal([2, 4, 6, 2, 5]) == 13  # 2 + 6 + 5
    assert sum_non_adjacent_non_optimal([5, 1, 1, 5]) == 10  # 5 + 5
    assert sum_non_adjacent_non_optimal([3, 4, 5, 6]) == 10  # 4 + 6
    assert sum_non_adjacent_non_optimal([-3, -4, 5, 6]) == 6  # 6
    assert sum_non_adjacent_non_optimal([0, 2, 4, 5]) == 7  # 2 + 5

    assert sum_non_adjacent_optimal([2, 4, 6, 2, 5]) == 13
    assert sum_non_adjacent_optimal([5, 1, 1, 5]) == 10
    assert sum_non_adjacent_optimal([3, 4, 5, 6]) == 10
    assert sum_non_adjacent_optimal([-3, -4, 5, 6]) == 6
    assert sum_non_adjacent_optimal([0, 2, 4, 5]) == 7
    
    print("Successfully tested.")
