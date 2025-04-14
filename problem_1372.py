"""1372. Longest ZigZag Path in a Binary Tree


You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
"""


def longestZigZag(self, root: Optional[TreeNode]) -> int:
  self.maxLength = 0
  def solve(node, deep, dir):
      self.maxLength = max(self.maxLength, deep)

      if node.left is not None:
          solve(node.left, deep+1,'left') if dir != 'left' else solve(node.left, 1, 'left')
      if node.right is not None:
          solve(node.right, deep+1, 'right') if dir != 'right' else solve(node.right, 1, 'right')
  solve(root, 0, '')
  return self.maxLength