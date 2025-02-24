"""645. Set Mismatch


You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""

from collections import Counter


def findErrorNums(self, nums: list[int]) -> list[int]:
  c=Counter(nums)
  l=[0,0]
  for i in range(1,len(nums)+1):
      if c[i]==2:
          l[0]=i
      if c[i]==0:
          l[1]=i
  return l