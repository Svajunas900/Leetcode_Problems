"""1800. Maximum Ascending Subarray Sum


Given an array of positive integers nums, 
return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] 
is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.
"""

def maxAscendingSum(nums: list[int]) -> int:
  max_sum = nums[0]
  result = max_sum
  if len(nums) == 0:
      return 0
  if len(nums) < 2:
      return nums[0]
  for i in range(1, len(nums)):
      if nums[i-1] >= nums[i]:
          max_sum = nums[i]
      else:
          max_sum += nums[i]
      result = max(result, max_sum)
  return result 