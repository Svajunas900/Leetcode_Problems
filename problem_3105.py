"""3105. Longest Strictly Increasing or Strictly Decreasing Subarray


You are given an array of integers nums. Return the length of the longest 
subarray of nums which is either strictly increasing or strictly decreasing Strictly Decreasing Array
An array is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).
"""

def longestMonotonicSubarray(self, nums: list) -> int:
  nums_length, result, inc, dec = len(nums), 0, 1, 1
  if nums_length == 1: return 1
  for i in range(1, nums_length):
      if nums[i-1] < nums[i]:
          inc += 1
          dec = 1
      elif nums[i-1] > nums[i]:
          inc = 1
          dec += 1
      else:
          inc = 1
          dec = 1
      result = max(result, inc, dec)
  return result