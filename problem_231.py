"""231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

def isPowerOfTwo(n: int) -> bool:
    if n == 2 or n == 1:
        return True
    s = 2
    while s <= n:
        if s == n:
            return True
        s *= 2
    return False