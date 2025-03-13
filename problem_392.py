"""392. Is Subsequence


Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


def isSubsequence(self, s: str, t: str) -> bool:
  if len(s) > len(t):
      return False
  if len(s) == 0:
      return True
  pointer = 0
  last_char = len(s) - 1
  for char in t:
      if pointer == last_char and s[pointer] == char:
          return True
      if s[pointer] == char:
          pointer += 1
  return False