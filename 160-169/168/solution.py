"""
Problem 168 [MEDIUM]

This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?
"""
from typing import List


def rotate_90_degrees_clockwise_naive(matrix: List[List[int]]):
    """
    Creates a new matrix, processing the original in this order:
    - start with first col, last row
    - read elements in vertical descending: rowN,col0 -> rowN-1, col0, rowN-2, col0...
    - iterate but starting from the next column
    Time: O(n^2), Space: O(n^2)
    """

    rotated_matrix: List[List[int]] = []
    matrix_size = len(matrix)

    for row in range(0, matrix_size):
        rotated_matrix.append([])
        for col in range(0, matrix_size):
            rotated_matrix[row].append(matrix[matrix_size-col-1][row])

    return rotated_matrix


def rotate_90_degrees_clockwise_no_extra_space(matrix: List[List[int]]):
    """
    4 movements in each iteration.
    No need to go through all rows (bottom rows get updated) neither to get to the last column.
    Solution doesn't use extra space.
    Time: O(n^2), Space: O(1)
    """
    matrix_size = len(matrix)

    for i in range(0, matrix_size//2):
        for j in range(i, matrix_size-i-1):
            p_0 = matrix[i][j]
            p_1 = matrix[j][matrix_size-i-1]
            p_2 = matrix[matrix_size-i-1][matrix_size-j-1]
            p_3 = matrix[matrix_size-j-1][i]

            matrix[i][j] = p_3
            matrix[j][matrix_size-i-1] = p_0
            matrix[matrix_size-i-1][matrix_size-j-1] = p_1
            matrix[matrix_size-j-1][i] = p_2

    return matrix


if __name__ == "__main__":
    challenges: list = [
        {
            "original": [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]],
            "rotated": [[13,9,5,1], [14,10,6,2], [15,11,7,3], [16,12,8,4]]
        },
        {
            "original": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "rotated": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        },        
        {
            "original": [[1,2], [3,4]],
            "rotated": [[3,1], [4,2]]
        },
        {
            "original": [[1]],
            "rotated": [[1]]
        },
        {
            "original": [],
            "rotated": []
        }
    ]

    for challenge in challenges:
        rotated_naive =  rotate_90_degrees_clockwise_naive(challenge["original"])
        rotated_efficient = rotate_90_degrees_clockwise_no_extra_space(challenge["original"])
        for row in range(0, len(challenge["rotated"])):
            for col in range(0, len(challenge["rotated"])):
                assert challenge["rotated"][row][col] == rotated_naive[row][col]
                assert challenge["rotated"][row][col] == rotated_efficient[row][col]

    print("Successfully tested.")
