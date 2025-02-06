"""47. Permutations II


Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.
"""

def permuteUnique(self, nums: list[int]) -> list[list[int]]:
  def helper(nums, perm=[], res=[]):
      if not nums:
          if perm not in res:
              res.append(perm[::])
      for i in range(len(nums)):
          num = nums[:i] + nums[i+1:]
          perm.append(nums[i])
          helper(num,perm,res)
          perm.pop()
      return res
  return helper(nums)