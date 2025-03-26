"""2033. Minimum Operations to Make a Uni-Value Grid

You are given a 2D integer grid of size m x n and an integer x. 
In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
"""

def minOperations(grid: list[list[int]], x: int) -> int:
      values = sorted([val for row in grid for val in row])
      diff = [abs(val - values[0]) % x for val in values]
      if any(d != 0 for d in diff):
          return -1
      median = values[len(values) // 2] 
      operations = sum(abs(val - median) // x for val in values)

      return operations   