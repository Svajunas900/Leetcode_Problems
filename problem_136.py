"""136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


def singleNumber(nums: list) -> int:
    uniqNum = 0
    for idx in nums:
        uniqNum ^= idx
    return uniqNum; 

print(singleNumber([4,1,2,1,2]))