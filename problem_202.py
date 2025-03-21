"""202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""
"""Time complexity Big O(n)

Space complexity Big O(n)
"""
def isHappy(n: int) -> bool:
    dummy = n
    visited = set()
    while dummy not in visited:
        visited.add(dummy)
        res = 0
        for i in str(dummy):
            res += int(i)**2
        dummy = res
        if dummy == 1:
            return True
    return False
