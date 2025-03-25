"""1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

def uniqueOccurrences(arr: list[int]) -> bool:
  counter = {}
  for i in arr:
      if i not in counter:
          counter[i] = 1
      else:
          counter[i] += 1
  result = []
  for key, value in counter.items():
      result.append(value)
  return len(set(result)) == len(result)