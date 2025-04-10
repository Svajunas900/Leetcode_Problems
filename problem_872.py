"""872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, 
the values of those leaves form a leaf value sequence.
"""


# DFS Solution
def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
  leafs_1 = self.dfs(root1, [])
  leafs_2 = self.dfs(root2, [])
  return leafs_1 == leafs_2

def dfs(self, root, leafs):
  if not root:
      return None
  self.dfs(root.left, leafs)
  self.dfs(root.right, leafs)
  if not root.right and not root.left:
      leafs.append(root.val)
  return leafs