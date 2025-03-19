"""1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""
def longestSubarray(nums: list[int]) -> int:
  counter = 1
  left = 0
  max_sub = 0
  for right in range(len(nums)):
      if nums[right] == 0:
          if counter == 0:
              while nums[left] != 0:
                  left += 1
              left += 1
          else:
              counter -= 1
      max_sub = max(max_sub, right-left)
  return max_sub

longestSubarray([0,1,1,1,0,1,1,0,1])