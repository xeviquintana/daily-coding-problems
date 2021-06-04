""" 
[HARD]
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def product_array_division(arr: [int]) -> [int]:
    """
    Compute product of all elements => p_all
    New array will have each element at position i in original array, p_all/arr[i]
    O(2N) in time, O(N) in space
    """
    p_all: int = 1

    for n in arr:
        p_all *= n

    return [p_all / n for n in arr]


def product_array_no_division(arr: [int]) -> [int]:
    """
    result[i] => product of arr[0] to arr[i-1] times
                 product of arr[i+1] to arr[len(arr)-1] (or arr[-1], last element)
    
    Given [2,4,6]:
        position 0 >>> left(1) * right(24) = 24
        position 1 >>> left(2) * right(6) = 12
        position 2 >>> left(8) * right(1) = 8
        result is [24, 12, 8]
    O(N^2) in time, O(N) in space
    """
    product: [int] = []

    for i, _ in enumerate(arr):
        left: int = 1
        right: int = 1
        for l in arr[:i]:
            left *= l
        for r in arr[i+1:]:
            right *= r
        product.append(left * right)

    return product


if __name__ == '__main__':
    assert product_array_division([]) == []
    assert product_array_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_array_division([3, 2, 1]) == [2, 3, 6]
    assert product_array_division([1, 2, 3, -1, -2]) == [12, 6, 4, -12, -6]

    assert product_array_no_division([]) == []
    assert product_array_no_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_array_no_division([3, 2, 1]) == [2, 3, 6]
    assert product_array_no_division([1, 2, 3, -1, -2]) == [12, 6, 4, -12, -6]
    print("Successfully tested.")
