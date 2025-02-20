"""171. Excel Sheet Column Number


Given a string columnTitle that represents the column title as appears in an Excel sheet, 
return its corresponding column number.
"""

def titleToNumber(columnTitle: str) -> int:
  col_num = 0
  for char in columnTitle:
      col_num = col_num * 26 + (ord(char) - 64)
  return col_num