"""441. Arranging Coins

You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
"""

def arrangeCoins(self, n: int) -> int:
  left,right=1,n
  while left<=right:
      mid=(right+left)//2
      num=(mid/2)*(mid+1)
      if num<=n:
          left=mid+1
      else:
          right=mid-1
  return right