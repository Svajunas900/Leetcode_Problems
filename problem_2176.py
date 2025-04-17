"""2176. Count Equal and Divisible Pairs in an Array

Given a 0-indexed integer array nums of length n and an integer k, 
return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
"""


def countPairs(self, nums: list[int], k: int) -> int:
    counter = 0
    for i in range(len(nums)):
        for x in range(i+1, len(nums)):
            if nums[i] == nums[x] and (i * x) % k == 0:
                counter += 1
    return counter
