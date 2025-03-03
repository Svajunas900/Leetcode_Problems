"""1768. Merge Strings Alternately


You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Return the merged string
"""

def mergeAlternately(word1: str, word2: str) -> str:
  result = ""
  length_1 = len(word1)
  length_2 = len(word2)
  for i in range(max(length_1, length_2)):
      if i < length_1:
          result += word1[i]
      if i < length_2:
          result += word2[i]
  return result