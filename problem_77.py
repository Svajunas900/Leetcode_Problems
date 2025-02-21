"""77. Combinations


Given two integers n and k, 
return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""
def combine(self, n: int, k: int) -> list[list[int]]:
  result = []
  combinations = []
  def backtrack(start):
      if len(combinations) == k:
          result.append(combinations[:])
          return
      for i in range(start, n+1):
          combinations.append(i)
          backtrack(i+1)
          combinations.pop()
  backtrack(1)
  return result