"""2226. Maximum Candies Allocated to K Children

You are given a 0-indexed integer array candies. 
Each element in the array denotes a pile of candies of size candies[i]. 
You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. 
You should allocate piles of candies to k children such that each child gets 
the same number of candies. 
Each child can be allocated candies from only one pile of candies and 
some piles of candies may go unused.

Return the maximum number of candies each child can get.
"""
def maximumCandies(candies: list[int], k: int) -> int:
  left, right = 1, max(candies)
  result = 0
  
  while left <= right:
      mid = (left + right) // 2
      
      children_count = sum(pile // mid for pile in candies)
      
      if children_count >= k:
          result = mid
          left = mid + 1
      else:
          right = mid - 1
          
  return result