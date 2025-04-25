"""2845. Count of Interesting Subarrays

You are given a 0-indexed integer array nums, an integer modulo, and an integer k.

Your task is to find the count of subarrays that are interesting.

A subarray nums[l..r] is interesting if the following condition holds:

Let cnt be the number of indices i in the range [l, r] such that nums[i] % modulo == k. Then, cnt % modulo == k.
Return an integer denoting the count of interesting subarrays.

Note: A subarray is a contiguous non-empty sequence of elements within an array.
"""
from collections import defaultdict


def count_interesting_subarrays(nums: list[int], modulo: int, k: int) -> int:
    count = 0
    equals = 0
    mpp = defaultdict(int)
    mpp[0] = 1
    for i in nums:
        if i % modulo == k:
            equals += 1
        rem = equals % modulo
        needed = (rem - k + modulo) % modulo
        count += mpp[needed]
        mpp[rem] += 1
    return count


count_interesting_subarrays([3, 2, 4], 2, 1)
