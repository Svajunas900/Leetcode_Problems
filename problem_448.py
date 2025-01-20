"""448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""

def findDisappearedNumbers(self, nums: list) -> list:
  s = set(nums)
  return [i for i in range(1,len(nums)+1) if i not in s]