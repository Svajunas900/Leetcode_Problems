"""283. Move Zeroes


Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
def moveZeroes(nums: list[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  left = 0
  right = 0
  while right < len(nums):
      if nums[right] != 0:
          nums[left], nums[right] = nums[right], nums[left]
          left += 1
      right += 1