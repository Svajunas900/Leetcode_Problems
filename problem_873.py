"""873. Length of Longest Fibonacci Subsequence

A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, 
return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, 
without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
"""

def lenLongestFibSubseq(arr: list[int]) -> int:
  n = len(arr)
  dp = [[0] * n for _ in range(n)]
  maxLen = 0

  for curr in range(2, n):
      start, end = 0, curr - 1
      while start < end:
          pairSum = arr[start] + arr[end]
          if pairSum > arr[curr]:
              end -= 1
          elif pairSum < arr[curr]:
              start += 1
          else:
              dp[end][curr] = dp[start][end] + 1
              maxLen = max(dp[end][curr], maxLen)
              end -= 1
              start += 1

  return 0 if maxLen == 0 else maxLen + 2