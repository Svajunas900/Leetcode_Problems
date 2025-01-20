"""94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

"""Time complexity Big O(n)

Space complexity Big O(n)
"""
def inorderTraversal(root) -> list:
  result = []
  def inorder(root):
      if not root:
          return []
      inorder(root.left)
      result.append(root.val)
      inorder(root.right)
      return result
  inorder(root)
  return result
