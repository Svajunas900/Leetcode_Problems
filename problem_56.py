"""56. Merge Intervals


Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

def merge(intervals: list[list[int]]) -> list[list[int]]:
  intervals.sort()
  result = []
  prev = intervals[0]
  for interval in intervals[1:]:
      if interval[0] <= prev[1]:
          prev[1] = max(prev[1], interval[1])
      else:
          result.append(prev)
          prev = interval
  result.append(prev)
  return result