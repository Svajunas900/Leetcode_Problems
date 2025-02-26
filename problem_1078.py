"""1078. Occurrences After Bigram


Given two strings first and second, 
consider occurrences in some text of the form "first second third",
where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".
"""
def findOcurrences(text: str, first: str, second: str) -> list[str]:
  ans = []
  words = text.split(' ')
  for i in range(2, len(words)):
      if words[i - 2] == first and words[i - 1] == second:
          ans.append(words[i])
  return ans