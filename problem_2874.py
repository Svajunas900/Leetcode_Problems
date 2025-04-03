"""2874. Maximum Value of an Ordered Triplet II

You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. 
If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
"""

def maximumTripletValue(nums: list[int]) -> int:
  maxi = float('-inf')
  diff = 0
  res = 0
  for i in range(len(nums)):
      maxi = max(maxi, nums[i])
      if i >= 2:
          res = max(res, diff * nums[i])
      if i >= 1:
          diff = max(diff, maxi - nums[i])  
  return res
  