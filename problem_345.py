"""345. Reverse Vowels of a String


Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

def reverseVowels(s: str) -> str:
  list_s = list(s)
  s = s.lower()
  left, right = 0, len(s)-1
  vowels = ["a", "e", "i", "o", "u"]
  while left < right:
      if s[left] in vowels:
          while s[right] not in vowels:
              right -= 1
          list_s[left], list_s[right] = list_s[right], list_s[left]
          right -= 1
      left += 1
  return ''.join(list_s)