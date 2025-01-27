"""13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

"""Time complexity Big O(n)
The dominant operation is going through all len in s
Space complexity Big O(1)
prev, result, roman are constant space
"""

def romanToInt(s: str) -> int:
  roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
  }
  if len(s) < 2:
      return roman[s]
  prev = s[0]
  result = roman[prev]
  for i in range(1, len(s)):
      curr = s[i]
      if prev == "I" and curr == "V" or prev == "I" and curr == "X":
          result += roman[curr] - 2
      elif prev == "X" and curr == "L" or prev == "X" and curr == "C":
          result += roman[curr] - 20
      elif prev == "C" and curr == "D" or prev == "C" and curr == "M":
          result += roman[curr] - 200
      else:
          result += roman[curr]
      prev = curr
  return result

print(romanToInt("MCMXCIV"))