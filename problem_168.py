"""168. Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
"""

def convertToTitle(columnNumber: int) -> str:
  result = ""
  while columnNumber > 0:
      result = chr(ord("A") + (columnNumber - 1) % 26) + result
      columnNumber = (columnNumber - 1) // 26
  return result