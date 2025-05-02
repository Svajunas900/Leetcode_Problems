"""1295. Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even number of digits.
"""

def findNumbers(self, nums: list[int]) -> int:
      counter = 0
      for num in nums:
          if not len(str(num)) % 2:
              counter += 1
      return counter