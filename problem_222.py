"""222. Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, 
is completely filled in a complete binary tree, 
and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
"""


def countNodes(self, root: Optional[TreeNode]) -> int:
  if not root:
      return 0
  leftDepth = self.getDepth(root.left)
  rightDepth = self.getDepth(root.right)
  if leftDepth == rightDepth:
      return pow(2, leftDepth) + self.countNodes(root.right)
  else:
      return pow(2, rightDepth) + self.countNodes(root.left)

def getDepth(self, root):
  if not root:
      return 0
  return 1 + self.getDepth(root.left)