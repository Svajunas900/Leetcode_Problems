"""66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
he digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

def plusOne(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]+1 != 10:
            digits[i] += 1
            return digits
        digits[i] = 0
        if i == 0:
            return [1] + digits


# One string solution with using the list comprehension
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in str(int("".join([str(x) for x in digits])) + 1)]
