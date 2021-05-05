"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def add_up_to_k_naive(arr: [int], k: int) -> bool:
    """
    First loop the array.
        - For every element at position i, check against every element in the array starting from element at i+1

    O(n * log(n)) in time, O(1) in space
    """
    for idx, n in enumerate(arr):
        for m in arr[idx+1:]:
            if n + m == k:
                return True

    return False


def add_up_to_k(arr: [int], k: int) -> bool:
    """
    How can we do it in one pass?
    We need to check if, for a number in arr, there's such a number in arr that satisfies 'k minus n is in arr'
    For that, we need to store each number we process in a fast lookup data structure.
    Special attention to 'halves': we need 2 halves.
        >> add_up_to_k(arr: [1, 5, 10, 11], k: 20) should return False
        >> add_up_to_k(arr: [1, 5, 10, 10], k: 20) should return True

    O(n) in time, 0(n) in space
    """
    processed: dict = {}
    for num in arr:
        processed[num] = 1 if num not in processed else processed[num] + 1
        if k-num not in processed:
            continue

        if k-num != num and processed[k-num] == 1:
            return True
        elif k-num == num and processed[k-num] == 2:
            return True

    return False


if __name__ == '__main__':
    assert add_up_to_k([], k=1) == False
    assert add_up_to_k([1], k=1) == False
    assert add_up_to_k([10, 15, 3, 7], k=17) == True
    assert add_up_to_k([5, 3, 10], k=20) == False
    assert add_up_to_k([5, 3, 10, 10], k=20) == True
    assert add_up_to_k([5, 3, 10, 10, 10], k=30) == False

    print("Successfully tested.")
