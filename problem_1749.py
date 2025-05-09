"""1749. Maximum Absolute Sum of Any Subarray


You are given an integer array nums. 
The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
"""
def maxAbsoluteSum(nums: list[int]) -> int:
  curr, max_val = 0, float('-inf')
  n = len(nums)

  for i in range(n):
      curr = max(0, curr + nums[i])
      max_val = max(max_val, curr)

  curr, min_val = 0, float('inf')
  
  for i in range(n - 1, -1, -1):
      curr = min(0, curr + nums[i])
      min_val = min(min_val, curr)
  
  return max(max_val, abs(min_val))