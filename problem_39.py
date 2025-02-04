"""39. Combination Sum


Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]: 
  def _helper(candidates, target, combination=[], result=[]):
      if sum(combination) > target:
          return
      sorted_comb = sorted(combination)
      if sum(combination) == target and sorted_comb not in result:
          result.append(sorted_comb[::])
      for cand in candidates:
          combination.append(cand)
          _helper(candidates, target, combination, result)
          combination.pop()
      return result
  return _helper(candidates, target)


print(combinationSum([2,3,5], 8))