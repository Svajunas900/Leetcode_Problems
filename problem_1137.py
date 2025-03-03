"""1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""


def tribonacci(n: int) -> int:
  memo = {}
  def _helper(n):
      if n in memo:
          return memo[n]
      if n == 0:
          return 0
      if n == 1 or n == 2:
          return 1
      result = _helper(n-1) + _helper(n-2) + _helper(n-3)
      memo[n] = result
      return result
  return _helper(n)