"""394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], 
where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; 
there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
"""

def decodeString(s: str) -> str:
  stack = []; curNum = 0; curString = ''
  for c in s:
      if c == '[':
          stack.append(curString)
          stack.append(curNum)
          curString = ''
          curNum = 0
      elif c == ']':
          num = stack.pop()
          prevString = stack.pop()
          curString = prevString + num*curString
      elif c.isdigit():
          curNum = curNum*10 + int(c)
      else:
          curString += c
  return curString