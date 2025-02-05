"""1790. Check if One String Swap Can Make Strings Equal


You are given two strings s1 and s2 of equal length. 
A string swap is an operation where you choose two indices in a string 
(not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal 
by performing at most one string swap on exactly one of the strings. Otherwise, return false.
"""



def areAlmostEqual(s1: str, s2: str) -> bool:
  length_of_s1 = len(s1)
  length_of_s2 = len(s2)
  counter = 0
  first = ""
  second = ""
  first_2 = ""
  second_2 = ""        
  if length_of_s1 != length_of_s2:
      return False
  for i in range(length_of_s1):
      if s1[i] != s2[i]:
          counter += 1
          if counter == 1:
              first = s1[i]
              first_2 = s2[i]
          if counter == 2:
              second = s1[i]
              second_2 = s2[i]
  if first != second_2 or second != first_2:
      return False
  if counter > 2:
      return False
  if counter == 2:
      return True
  return s1 == s2