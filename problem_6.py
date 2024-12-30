"""6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
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