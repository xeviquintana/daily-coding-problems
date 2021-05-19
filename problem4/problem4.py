"""
PROBLEM #4 [HARD]

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def first_missing_positive_integer(arr: [int]) -> int:
    """
    We divide the array into 2 parts such that the first part consists of only positive numbers.
    Say we have the starting index as 0 and the ending index as end(exclusive).

    We traverse the array from index 0 to end. We take the absolute value of the element at that index - say the value is x.

    If x > end we do nothing.
    If not, we make the sign of the element at index x-1 negative.
    Finally, we traverse the array once more from index 0 to end. In case we encounter a positive element at some index, we output index + 1. This is the answer.
    However, if we do not encounter any positive element, it means that integers 1 to end occur in the array. We output end + 1.
    """
    positives: [int] = [n for n in arr if n > 0]  # create an array of positive values only
    
    for n in positives:
        abs_n: int = abs(n)  # we can have negative values after processing the "original" positives array
        if abs_n -1 >= len(positives):  # array won't be reachable with that index
            continue

        idx: int = abs_n-1  # Let a zero-based index be the absolute value of the int - 1
        if idx < 0 or idx > len(positives):  # array won't be reachable with that index
            continue

        if positives[idx] > 0:
            positives[idx] = -1 * positives[idx]  # turn negative
    
    for i, k in enumerate(positives):
        if k > 0:
            return i + 1
    
    return len(positives) + 1


if __name__ == "__main__":
    assert first_missing_positive_integer([3, 4, -1, 1]) == 2
    assert first_missing_positive_integer([1, 2, 0]) == 3
    assert first_missing_positive_integer([1, 2, 3, 5, 6]) == 4
    assert first_missing_positive_integer([4, 1, 3]) == 2
    print("Successfully tested.")
