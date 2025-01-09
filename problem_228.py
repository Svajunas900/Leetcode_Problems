"""228. Summary Ranges


You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

def summaryRanges(self, nums: list) -> list:
  ranges = [] # [start, end] or [x, y]
  for n in nums:
      if ranges and ranges[-1][1] == n-1:
          ranges[-1][1] = n
      else:
          ranges.append([n, n])

  return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]