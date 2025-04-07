"""416. Partition Equal Subset Sum


Given an integer array nums, return true if you can partition the array into two 
subsets such that the sum of the elements in both subsets is equal or false otherwise.
"""

def canPartition(nums: list[int]) -> bool:
  totalSum = sum(nums)
  if totalSum % 2 != 0:
      return False
  targetSum = totalSum // 2
  dp = [False] * (targetSum + 1)
  dp[0] = True
  for num in nums:
      for currSum in range(targetSum, num - 1, -1):
          dp[currSum] = dp[currSum] or dp[currSum - num]
  return dp[targetSum]