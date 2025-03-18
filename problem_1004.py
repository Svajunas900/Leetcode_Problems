"""1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

def longestOnes(nums: list[int], k: int) -> int:
  left = 0
  max_length = 0
  counter = 0
  for right in range(len(nums)):
      if nums[right] == 0:
          counter += 1
      while counter > k:
          if nums[left] == 0:
              counter -= 1
          left += 1
      max_length = max(max_length,right-left+1)
          
  return max_length 
