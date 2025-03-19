"""3191. Minimum Operations to Make Binary Array Elements Equal to One I

You are given a binary array nums.

You can do the following operation on the array any number of times (possibly zero):

Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
"""

def minOperations(nums: list[int]) -> int:
  counter = 0
  for right in range(2, len(nums)):
      left = right - 2
      if nums[left] == 0:
          counter += 1
          for i in range(left, right+1):
              if nums[i] == 0:
                  nums[i] = 1
              else:
                  nums[i] = 0
  for i in range(left, right+1):
      if nums[i] == 0:
          return -1
  return counter

minOperations([0,1,1,1])