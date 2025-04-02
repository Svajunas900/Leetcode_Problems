"""2873. Maximum Value of an Ordered Triplet I


You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. 
If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
"""

def maximumTripletValue(self, nums: list[int]) -> int:
  n = len(nums)
  leftMax = [0] * n
  rightMax = [0] * n
  leftMax[0] = nums[0]
  for i in range(1, n):
      leftMax[i] = max(leftMax[i - 1], nums[i])

  rightMax[n - 1] = nums[n - 1]
  for k in range(n - 2, -1, -1):
      rightMax[k] = max(rightMax[k + 1], nums[k])

  maxValue = 0
  for j in range(1, n - 1):
      value = (leftMax[j - 1] - nums[j]) * rightMax[j + 1]
      maxValue = max(maxValue, value)

  return maxValue