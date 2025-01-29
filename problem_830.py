"""830. Positions of Large Groups

In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], 
where start and end denote the start and end indices (inclusive) of the group. 
In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.
"""

def largeGroupPositions(self, s: str) -> List[List[int]]:
  result = []
  left, right = 0, 1
  if len(s) < 3:
      return result
  while right != len(s):
      if s[left] == s[right]:
          right += 1
      else:
          if right - left >= 3:
              result.append([left, right-1])
          left = right
          right += 1 
  if right - left >= 3:
      result.append([left, right-1])
  return result