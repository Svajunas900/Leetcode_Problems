"""415. Add Strings


Given two non-negative integers, num1 and num2 represented as string, 
return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.
"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""

def addStrings(num1: str, num2: str) -> str:
  length_of_num1 = len(num1) - 1
  length_of_num2 = len(num2) - 1
  carry = 0
  sum_of_nums = []
  while length_of_num1 >= 0 or length_of_num2 >= 0 or carry:
      digit1 = ord(num1[length_of_num1]) - ord("0") if length_of_num1 >= 0 else 0
      digit2 = ord(num2[length_of_num2]) - ord("0") if length_of_num2 >= 0 else 0
      total = digit1 + digit2 + carry
      carry = total // 10
      sum_of_nums.append(str(total % 10))
      length_of_num1 -= 1
      length_of_num2 -= 1
  return ''.join(sum_of_nums[::-1])