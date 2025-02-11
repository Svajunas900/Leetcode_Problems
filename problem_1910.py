"""1910. Remove All Occurrences of a Substring


Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.
"""

def removeOccurrences(s: str, part: str) -> str:
  while part in s:
      s = s.replace(part, "", 1)  
  return s