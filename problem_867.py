"""867. Transpose Matrix


Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the matrix's row and column indices.
"""

def transpose(matrix: list[list[int]]) -> list[list[int]]:
  result = [[0] * len(matrix) for _ in range(len(matrix[0]))]
  for row in range(len(matrix)):
      for column in range(len(matrix[row])):
          result[column][row] = matrix[row][column]
  return result