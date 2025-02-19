"""118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""
def generate(numRows: int) -> list:
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    
    prevRows = generate(numRows-1)
    newRow = [1] * numRows

    for i in range(1, numRows-1):
        newRow[i] = prevRows[-1][i-1] + prevRows[-1][i]
    
    prevRows.append(newRow)
    return prevRows

