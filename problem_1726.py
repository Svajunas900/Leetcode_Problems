"""1726. Tuple with Same Product


Given an array nums of distinct positive integers, 
return the number of tuples (a, b, c, d) such that a * b = c * d 
where a, b, c, and d are elements of nums, and a != b != c != d
"""
from collections import defaultdict



def tupleSameProduct(nums: list[int]) -> int:
  product_count = defaultdict(int)
  ans = 0

  for i in range(len(nums)):
      for j in range(i+1, len(nums)):
          product = nums[i] * nums[j]
          ans += 8 * product_count[product]
          product_count[product] += 1

  return ans

print(tupleSameProduct([1,2,4,5,10]))
