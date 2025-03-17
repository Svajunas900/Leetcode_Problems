"""1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""

def maxVowels(s: str, k: int) -> int:
  vowels = {'a', 'e', 'i', 'o', 'u'}
  curr = 0 
  for i in range(k): 
      if s[i] in vowels:
          curr += 1
  max_vowels = curr 
  for i in range(k, len(s)):
      if s[i] in vowels:
          curr += 1
      if s[i-k] in vowels:
          curr -= 1
      max_vowels = max(max_vowels, curr) 
  return max_vowels

print(maxVowels("pdzndkhhoujpqyex", 5))
        