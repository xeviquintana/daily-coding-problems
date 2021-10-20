"""
PROBLEM 18 [HARD]

This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get:
[10, 7, 8, 8], since:

- 10 = max(10, 5, 2)
- 7 = max(5, 2, 7)
- 8 = max(2, 7, 8)
- 8 = max(7, 8, 7)

Do this in O(n) time and O(k) space.
You can modify the input array in-place and you do not need to store the
results. You can simply print them out as you compute them.
"""

from typing import Deque, List


def max_in_subarray(arr: List[int], k: int) -> List[int]:
    """
    Solution keeps a deque (O(1) in pop/append operations from both sides)
    Deque keeps greatest element's index on the left, lowest on the right.
    Operations per loop:
        Discards current max if it is out of range
        Discards current max if current index value is greater than current max.
        Discards current min if it is lower than current index value.
        If deque is empty or current index value is lower than min, appends it on the right.
    """
    if k <= 0:
        raise ValueError("k needs to be positive")
    if k == 1:
        return arr
    if not arr:
        return []

    deq: Deque = Deque()
    result: List[int] = []  # not needed, but it's easier to test by returning a result
    for i in range(k):
        if deq and arr[i] > arr[deq[0]]:
            deq.pop()
        deq.append(i)

    result.append(arr[deq[0]])
    for i in range(k, len(arr)):
        if deq[0] <= (i - k):  # current max is out of range, remove it
            deq.popleft()
        elif arr[i] > arr[deq[0]]:  # new max, previous max will be useless
            deq.popleft()
            deq.appendleft(i)
        elif arr[deq[-1]] < arr[i]:  # greater min, previous min will be useless
            deq.pop()
            deq.append(i)
        else:  # lower min, append it without discarding previous min as it can become a new max
            deq.append(i)

        result.append(arr[deq[0]])

    return result


if __name__ == "__main__":
    assert max_in_subarray([10,5,2,7,8,7], 3) == [10, 7, 8, 8]
    assert max_in_subarray([1,2,3,4,5,6], 3) == [3, 4, 5, 6]
    assert max_in_subarray([6,5,4,3,2,1], 3) == [6, 5, 4, 3]
    assert max_in_subarray([10,5,2,7,8,7], 1) == [10,5,2,7,8,7]
    assert max_in_subarray([], 2) == []
    print("Successfully tested.")
