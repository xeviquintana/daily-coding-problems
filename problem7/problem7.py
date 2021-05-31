"""
PROBLEM #7 [MEDIUM]

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def decode(num: int) -> int:
    """
    The number needs to be tested position by position,
    but groupings must be size 2 (as alphabet is from 1 to 26)

    O(n^2) in time, 0(n) in space
    """
    strnum: str = str(num)

    if len(strnum) == 1:
        return decodable(strnum)
    elif len(strnum) == 2:
        if strnum[0] == '0':
            return decodable(strnum)
        else:
            return 1 + decodable(strnum)
    else:
        return decodable(strnum[:2]) * decode(int(strnum[2:])) + decodable(strnum[:1]) * decode(int(strnum[1:]))
    # /if
# /def

def decodable(num: str) -> bool:
    """
    This functions checks if a string is a valid representation
    of what we consider an encoded message.
    Anything that's not a string representing an integer between
    1 and 26, inclusive, is not considered decodable.
    """

    if num == '' or num[0] == '0':
        return 0
    elif 0 < int(num) <= 26:
        return 1
    else:
        return 0
    # /if
# /def


if __name__ == "__main__":
    """
    a=1     b=2     c=3     d=4     e=5     f=6     g=7     h=8     i=9     j=10
    k=11    l=12    m=13    n=14    o=15    p=16    q=17    r=18    s=19    t=20
    u=21    v=22    w=23    x=24    y=25    z=26
    """
    assert decode(111) == 3, "Can be decoded as 'aaa', 'ka' and 'ak'"
    assert decode(26) == 2, "Can be decoded as 'bf' and 'z'"
    assert decode(262) == 2, "Can be decoded as 'bfb', 'zb'"
    assert decode(72) == 1, "Can be decoded as 'gb'"
    assert decode(1212) == 5, "Can be decoded as 'abab', 'lab', 'aub', 'abl' and 'll'"
    
    print("Successfully tested.")
