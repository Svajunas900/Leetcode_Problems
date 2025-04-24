"""2799. Count Complete Subarrays in an Array

You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.
"""


def count_complete_subarrays(nums: list[int]) -> int:
    total_unique = len(set(nums))
    count = 0
    left = 0
    freq = {}
    for right in range(len(nums)):
        if nums[right] in freq.keys():
            freq[nums[right]] += 1
        else:
            freq[nums[right]] = 1
        while len(freq) == total_unique:
            count += len(nums) - right
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1

    return count
