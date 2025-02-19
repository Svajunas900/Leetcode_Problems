"""1415. The k-th Lexicographical String of All Happy Strings of Length n


A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
"""

class Solution:
  def __init__(self):
      self.ans = ""

  def solve(self, length, k, n, chars, s):
      if length == n:
          k[0] -= 1
          if k[0] == 0:
              self.ans = s
          return
      for c in chars:
          if length == 0 or s[-1] != c:
              self.solve(length + 1, k, n, chars, s + c)
              if k[0] == 0:
                  return

  def getHappyString(self, n: int, k: int) -> str:
      self.ans = ""
      self.solve(0, [k], n, ['a', 'b', 'c'], "")
      return self.ans