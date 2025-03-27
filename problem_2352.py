"""2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""

def equalPairs(grid: list[list[int]]) -> int:
  columns = []
  for _ in range(len(grid)):
      columns.append([0] * len(grid))
  for row in range(len(grid)):
      for column in range(len(grid[row])):
          columns[row][column] = grid[column][row]
  counter = 0 
  for i in grid:
      if i in columns:
          counter += columns.count(i)
  return counter