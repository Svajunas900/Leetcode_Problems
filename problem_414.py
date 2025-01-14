"""414. Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.
"""


def thirdMax(self, nums: List[int]) -> int:
  if len(set(nums)) < 3:
      return max(nums)
  x = max(nums)
  nums.remove(max(nums))
  while(max(nums) == x):
      nums.remove(max(nums))
  y = max(nums)
  while(max(nums) == y):
      nums.remove(max(nums))
  return max(nums)