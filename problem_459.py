"""459. Repeated Substring Pattern


Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
"""


def repeatedSubstringPattern(self, s: str) -> bool:
  return s in (s + s)[1:-1]