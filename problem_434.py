"""434. Number of Segments in a String

Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.
"""

def countSegments(s: str) -> int:
  return len(s.split())