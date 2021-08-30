"""
PROBLEM 15 [MEDIUM]

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
from typing import TypeVar, Generic, List
import random

T: TypeVar = TypeVar('T')

def pick_one(big_stream: List[T]) -> T:
    # we can't store the array in memory, but we can process it
    # uniform probability -> each element should have the same chance to be picked up
    # >> a list of size = 1 needs to return the first element (100% chance)
    # >> a list of size = n, needs to return an element with 1/n chances

    rand_element: T = None
    for i, elem in enumerate(big_stream):
        if random.randint(1, i + 1) == 1:
            rand_element = elem

    return rand_element


if __name__ == "__main__":
    a_big_stream: List[int] = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    print("Randomly accessing {} -> got {}".format(a_big_stream, pick_one(a_big_stream)))
    print("Randomly accessing {} -> got {}".format(a_big_stream, pick_one(a_big_stream)))
    print("Randomly accessing {} -> got {}".format(a_big_stream, pick_one(a_big_stream)))
    print("Randomly accessing {} -> got {}".format(a_big_stream, pick_one(a_big_stream)))
    
    another_big_stream: List[str] = ['a', 'bc', 'def', 'ghij', 'klmno', 'pqrstu']
    print("Randomly accessing {} -> got {}".format(another_big_stream, pick_one(another_big_stream)))
    print("Randomly accessing {} -> got {}".format(another_big_stream, pick_one(another_big_stream)))
    print("Randomly accessing {} -> got {}".format(another_big_stream, pick_one(another_big_stream)))
    print("Randomly accessing {} -> got {}".format(another_big_stream, pick_one(another_big_stream)))
    print("Successfully tested.")
