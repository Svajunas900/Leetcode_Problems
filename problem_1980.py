"""1980. Find Unique Binary String


Given an array of strings nums containing n unique binary strings each of length n, 
return a binary string of length n that does not appear in nums. 
If there are multiple answers, you may return any of them.
"""

def findDifferentBinaryString(nums: list[str]) -> str:
  
  def backtrack(nums, result=[""]):
      if len(result[0]) == len(nums[0]):
        if result[0] not in nums:
          return result[0]
      if len(result[0]) > len(nums[0]):
         return 
      for i in ["0", "1"]:
          result[0] += i
          answer = backtrack(nums, result)
          result[0] = result[0][:-1]
          if answer:
            return answer
      return None
      
  return backtrack(nums)

print(findDifferentBinaryString(["00","01"]))