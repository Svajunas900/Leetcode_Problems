"""643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.
"""

def findMaxAverage(nums: list, k: int) -> float:
  result = 0
  left = 0
  right = k
  k_sum = sum(nums[left:right])
  avg = k_sum / k
  if len(nums) == k:
      return avg
  while right < len(nums):
      if result < avg or result == 0:
          result = avg
      left += 1
      k_sum = (k_sum - nums[left-1] + nums[right])
      avg = k_sum / k 
      right += 1
  if avg > result:
      return avg
  return result

print(findMaxAverage([1,12,-5,-6,50,3], 4))