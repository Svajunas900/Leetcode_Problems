"""40. Combination Sum II


Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""



def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
  ans = []
  ds = []
  candidates.sort()
  def findCombination(ind, target):
      if target == 0:
          ans.append(ds[:])
          return
      for i in range(ind, len(candidates)):
          if i > ind and candidates[i] == candidates[i - 1]:
              continue
          if candidates[i] > target:
              break
          ds.append(candidates[i])
          findCombination(i + 1, target - candidates[i])
          ds.pop()


  findCombination(0, target)
  return ans