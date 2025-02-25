"""268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""


def missingNumber(nums: list[int]) -> int:
  n = len(nums)
  ans = 0
  for i in range(1, n + 1):
      ans ^= i
  for num in nums:
      ans ^= num
  return ans