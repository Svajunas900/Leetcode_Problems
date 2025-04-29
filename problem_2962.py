"""2962. Count Subarrays Where Max Element Appears at Least K Times

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.
"""


def countSubarrays(self, nums: List[int], k: int) -> int:
    max_element = max(nums)
    res = 0
    left = maxi_count = 0

    for right in range(len(nums)):
        if nums[right] == max_element:
            maxi_count += 1
        while maxi_count == k:
            res += len(nums) - right
            if nums[left] == max_element:
                maxi_count -= 1
            left += 1

    return res
