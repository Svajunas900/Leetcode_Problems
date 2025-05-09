"""55. Jump Game


You are given an integer array nums. 
You are initially positioned at the array's first index,
 and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

def canJump(nums: list[int]) -> bool:
  goal = len(nums) - 1
  for i in range(len(nums) - 2, -1, -1):
      if nums[i] + i >= goal:
          goal = i
  return goal == 0
