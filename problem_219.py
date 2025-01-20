"""219. Contains Duplicate II

Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""

def containsNearbyDuplicate(nums:list, k: int) -> bool:
  hset = {}
  for idx in range(len(nums)):
      if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
          return True
      hset[nums[idx]] = idx
  return False