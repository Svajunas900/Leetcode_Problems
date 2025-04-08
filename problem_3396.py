"""3396. Minimum Number of Operations to Make Elements in Array Distinct

You are given an integer array nums. You need to ensure that the elements in the array are distinct. 
To achieve this, you can perform the following operation any number of times:

Remove 3 elements from the beginning of the array. 
If the array has fewer than 3 elements, remove all remaining elements.
Note that an empty array is considered to have distinct elements. 
Return the minimum number of operations needed to make the elements in the array distinct.
"""

def minimumOperations(nums: list[int]) -> int:
  seen = set()
  for i in range(len(nums)-1, -1, -1):
      if nums[i] in seen:
          return i // 3 + 1
      seen.add(nums[i])
  return 0