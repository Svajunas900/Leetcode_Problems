"""500. Keyboard Row

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
"""


def findWords(self, words: List[str]) -> List[str]:
  rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
  result = []
  row = None
  for word in words:
      if len(word) == 1:
          result.append(word)
          continue
      lowercase_word = word.lower()
      letter = lowercase_word[0]
      for idx, val in enumerate(rows): 
          if letter in val:
              row = idx
              break
      for i in range(1, len(lowercase_word)):
          if lowercase_word[i] not in rows[row]:
              break
          else:
              if i == len(lowercase_word)-1:
                  result.append(word)
              continue
          
  return result