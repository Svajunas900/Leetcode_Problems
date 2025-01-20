"""242. Valid Anagram


Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.
"""

"""Time complexity Big O(n)

Space complexity Big O(1)
"""

def isAnagram(s: str, t: str) -> bool:  
  if len(s) != len(t):
      return False
  for idx in set(s):
      if s.count(idx) != t.count(idx):
          return False
  return True