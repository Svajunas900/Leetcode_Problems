"""704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

def search(self, nums: List[int], target: int) -> int:
  left = 0
  right = len(nums) - 1
  while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
          return mid
      if nums[mid] < target:
          left = mid + 1
      if nums[mid] > target:
          right = mid - 1
  return -1 