"""3066. Minimum Operations to Exceed Threshold Value II


You are given a 0-indexed integer array nums, and an integer k.

In one operation, you will:

Take the two smallest integers x and y in nums.
Remove x and y from nums.
Add min(x, y) * 2 + max(x, y) anywhere in the array.
Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
"""
import heapq


def minOperations(nums: list[int], k: int) -> int:
  heapq.heapify(nums)
  res=0
  for i in range(0, len(nums)):
      x=heapq.heappop(nums)
      if x<k:
          res+=1
          y=heapq.heappop(nums)
          val= x*2+y if (x<y) else y*2+x
          heapq.heappush(nums, val)
      else:
          break
  return res


print(minOperations([2,11,10,1,3], 10))