"""6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
"""

"""Time complexity Big O(n)
It iterates through s making time complexity O(n)
Updating curRow and goingDown are O(1)
output joining all rows is O(n)

Space complexity Big O(n)
curRow and goingDown is equal to O(1)
rows is equal to input s or numRows making it O(n)
"""

def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [""] * min(numRows, len(s))
    curRow, goingDown = 0, False

    for c in s:
        rows[curRow] += c
        if curRow == 0 or curRow == numRows - 1:
            goingDown = not goingDown
        curRow += 1 if goingDown else -1
    
    return ''.join(rows)