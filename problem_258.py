"""258. Add Digits

Given an integer num, 
repeatedly add all its digits until the result has only one digit, 
and return it.
"""


def addDigits(self, num: int) -> int:
  if num == 0:
      return 0
  return 1 + (num - 1) % 9