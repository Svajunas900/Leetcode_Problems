"""2401. Longest Nice Subarray

You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.
"""

def longestNiceSubarray(nums: list[int]) -> int:
  n = len(nums)
  max_length = 1
  
  left = 0
  used_bits = 0
  
  for right in range(n):
      while used_bits & nums[right] != 0:
          used_bits ^= nums[left]
          left += 1
          
      used_bits |= nums[right]
      
      max_length = max(max_length, right - left + 1)
      
  return max_length

longestNiceSubarray([3,1,5,11,13])