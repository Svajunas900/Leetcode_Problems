"""2843. Count Symmetric Integers

You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric 
if the sum of the first n digits of x is equal to the sum of the last n digits of x. 
Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].

"""

def countSymmetricIntegers(low: int, high: int) -> int:
  counter = 0
  for num in range(low, high+1):
      num_list = list(str(num))
      length_num = len(num_list)
      if length_num % 2 == 1:
          continue
      mid = length_num // 2
      left = num_list[:mid]
      right = num_list[mid:]
      left_sum = 0
      right_sum = 0
      for i in range(mid):
          left_sum += int(left[i])
          right_sum += int(right[i])
      if left_sum == right_sum:
          counter += 1
  return counter