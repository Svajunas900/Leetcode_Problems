"""2375. Construct Smallest Number From DI String


You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions
"""


def smallestNumber(self, pattern: str) -> str:
  answer, temp = ["1"], []
  for i, val in enumerate(pattern):
      if val == "I":
          answer += temp[::-1] + [str(i+2)]
          temp = []
      else:
          temp.append(answer.pop())
          answer.append(str(i+2))
  return "".join(answer+temp[::-1])