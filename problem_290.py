"""290. Word Pattern


Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
"""


def wordPattern(pattern: str, s: str) -> bool:
  storage = {}
  words = s.split()
  if len(pattern) != len(words):
      return False
  for i in range(len(pattern)):
      if pattern[i] not in storage:
          storage[pattern[i]] = words[i]
      else: 
          if storage[pattern[i]] != words[i]:
              return False
  store = storage.values()
  set_values = set(store)
  if len(set_values) != len(store):
      return False
  return True


print(wordPattern("abba", "dog cat cat dog"))