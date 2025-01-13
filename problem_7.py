"""7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

def reverse(self, x: int) -> int:
  INT_MAX, INT_MIN = 2**31 - 1, -2**31
  reversed_x = 0
  sign = -1 if x < 0 else 1
  x = abs(x)
  
  while x != 0:
      pop = x % 10
      x //= 10
      if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and pop > 7):
          return 0
      reversed_x = reversed_x * 10 + pop
  
  return sign * reversed_x