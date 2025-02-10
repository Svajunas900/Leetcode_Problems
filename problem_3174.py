"""3174. Clear Digits


You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.
"""


def clearDigits(s: str) -> str:
  result = list(s)
  counter = 0
  for i in range(len(result)):
      if result[i-counter].isnumeric():
          result.pop(i-counter)
          if i != 0:
              result.pop(i-counter-1)
              counter += 2
  return "".join(result)


print(clearDigits("cb34"))