"""2529. Maximum Count of Positive Integer and Negative Integer


Given an array nums sorted in non-decreasing order, 
return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, 
then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.
"""


def maximumCount(nums: list[int]) -> int:
  pos_count = 0
  neg_count = 0
  for number in nums:
      if number > 0:
          pos_count += 1
      elif number == 0:
          continue
      else:
          neg_count += 1