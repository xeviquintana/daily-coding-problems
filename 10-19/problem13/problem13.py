"""
PROBLEM 13 [HARD]

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def distinct_characters(s: str, k: int) -> str:
    """
    Keep a sliding window of characters being processed. Maintain a set of this sliding window.
    Whenever the length of the set is greater than K, it means we need to check if current sliding window is greater
    than the longest string we found so far.
    Then, to continue processing remaining characters in S, we need to pop oldest elements of the sliding window as
    long as the size of its set is greater than K.
    In other words, the condition to start every loop is that length of set is acceptable: lower or equal than K.
    """
    substr = list()
    substr_set = set()
    longest = ""
    i = 0
    while i < len(s):
        current_char = s[i]
        substr_set.add(current_char)
        if len(substr_set) <= k:
            substr.append(current_char)
        else:
            if len(substr) > len(longest):
                longest = "".join(substr)
            substr.append(current_char)
            substr.pop(0)
            substr_set = set(substr)
            while len(substr_set) > k:
                substr.pop(0)
                substr_set = set(substr)
        i += 1
    
    if len(substr) > len(longest):
        longest = "".join(substr)
    
    return longest


if __name__ == "__main__":
    assert distinct_characters("abcba", 2) == "bcb"
    assert distinct_characters("abcd", 2) == "ab"
    assert distinct_characters("abcddd", 2) == "cddd"
    assert distinct_characters("abcdde", 2) == "cdd"
    assert distinct_characters("abcdee", 2) == "dee"
    assert distinct_characters("abbcddd", 2) == "cddd"
    assert distinct_characters("abcabc", 3) == "abcabc"
    
    print("Successfully tested.")
    
