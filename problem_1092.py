"""1092. Shortest Common Supersequence 


Given two strings str1 and str2, 
return the shortest string that has both str1 and str2 as subsequences. 
If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.
"""

def shortestCommonSupersequence(str1: str, str2: str) -> str:
  m, n = len(str1), len(str2)
  dp = [[0] * (n+1) for _ in range(m+1)]
  for i in range(1, m+1):
      for j in range(1, n+1):
          if str1[i-1] == str2[j-1]:
              dp[i][j] = 1 + dp[i-1][j-1]
          else:
              dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  i, j = m, n
  result = []
  while i > 0 and j > 0:
      if str1[i-1] == str2[j-1]:
          result.append(str1[i-1])
          i -= 1
          j -= 1
      elif dp[i-1][j] > dp[i][j-1]:
          result.append(str1[i-1])
          i -= 1
      else:
          result.append(str2[j-1])
          j -= 1
  while i > 0:
      result.append(str1[i-1])
      i -= 1
  while j > 0:
      result.append(str2[j-1])
      j -= 1
  return ''.join(result[::-1])

print(shortestCommonSupersequence("abac", "cab"))