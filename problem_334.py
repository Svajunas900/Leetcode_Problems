"""334. Increasing Triplet Subsequence

Given an integer array nums, 
return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
"""

def increasingTriplet(self, nums: list[int]) -> bool:
  first = float('inf')
  second = float('inf')
  for n in nums:
      if n <= first:
          first = n
      elif n <= second:
          second = n
      else:
          return True
  return False