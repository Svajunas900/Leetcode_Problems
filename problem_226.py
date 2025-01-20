"""226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.
"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
  if not root:
      return root
  self.invertTree(root.left)
  self.invertTree(root.right)
  root.left, root.right = root.right, root.left
  return root