"""2965. Find Missing and Repeated Values


You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. 
Each integer appears exactly once except a which appears twice and b which is missing. 
The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b
"""


def findMissingAndRepeatedValues(grid: list[list[int]]) -> list[int]:
  unique = set()
  length_of_grid = len(grid)
  values = length_of_grid**2
  result = []
  for row in range(len(grid)):
      for column in range(len(grid[row])):
          if grid[row][column] not in unique:
              unique.add(grid[row][column])
          else:
              result.append(grid[row][column])
  for i in range(1, values+1):
      if i not in unique:
          result.append(i)
  return result