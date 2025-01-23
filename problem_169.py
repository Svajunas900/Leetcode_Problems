"""169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""

"""Time complexity Big O(n log n)
Dominant operation nums.sort()

Space complexity Big O(1)
Only using constant space
"""

def majorityElement(nums: list) -> int:
  nums.sort()
  counter = 1
  for i in range(1, len(nums)):
      if nums[i-1] == nums[i]:
          counter += 1
      else:
          counter = 1
      if len(nums) / 2 < counter:
          return nums[i]
  return nums[0]

majorityElement([3,2,3])