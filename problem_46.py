"""46. Permutations

Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order.
"""

def permute(self, nums: List[int]) -> List[List[int]]:
  def dfs(nums, perm=[], res=[]):
      if len(nums) == 0:
          res.append(perm[::])
      for i in range(len(nums)):
          new_nums = nums[:i] + nums[i+1:]
          perm.append(nums[i])
          dfs(new_nums, perm, res)
          perm.pop()
      return res
  return dfs(nums)