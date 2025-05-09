"""2999. Count the Number of Powerful Integers


You are given three integers start, finish, and limit. 
You are also given a 0-indexed string s representing a positive integer.

A positive integer x is called powerful if it ends with s (in other words, s is a suffix of x) and each digit in x is at most limit.

Return the total number of powerful integers in the range [start..finish].

A string x is a suffix of a string y if and only if x is a substring of y that starts from some index (including 0) in y and extends to the index y.length - 1. 
For example, 25 is a suffix of 5125 whereas 512 is not.
"""

def numberOfPowerfulInt(start: int, finish: int, limit: int, s: str) -> int:
  def count(val:int) -> int:
      string_val = str(val)
      prefix = len(string_val) - len(s)
      if prefix < 0:
          return 0
      dp = [[0] * 2 for _ in range(prefix + 1)]  
      dp[prefix][0] = 1
      dp[prefix][1] = int(string_val[prefix:] >= s)

      for i in range(prefix - 1, -1, -1):
          digit = int(string_val[i])
          dp[i][0] = (limit + 1) * dp[i+1][0]
          if digit <= limit:
              dp[i][1] = digit * dp[i+1][0] + dp[i+1][1]
          else:
              dp[i][1] = (limit + 1) * dp[i+1][0]
      return dp[0][1]
  return count(finish) - count(start-1)

numberOfPowerfulInt(1, 6000, 4, "124")