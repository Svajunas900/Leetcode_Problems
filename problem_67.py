"""67. Add Binary

Given two binary strings a and b, return their sum as a binary string.
"""


def addBinary(a: str, b: str) -> str:
  res = []
  i, j = len(a) - 1, len(b) - 1
  carry = 0

  while i >= 0 or j >= 0:
      sum_ = carry
      if i >= 0:
          sum_ += int(a[i])
          i -= 1
      if j >= 0:
          sum_ += int(b[j])
          j -= 1
      carry = 1 if sum_ > 1 else 0
      res.append(str(sum_ % 2))
  
  if carry:
      res.append('1')
  return ''.join(res[::-1])