"""1123. Lowest Common Ancestor of Deepest Leaves

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, 
is the node A with the largest depth such that every node in S is in the subtree with root A.
"""

def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
  def dfs(node, depth):
      if not node:
          return (None, depth)
      
      left_lca, left_depth = dfs(node.left, depth + 1)
      right_lca, right_depth = dfs(node.right, depth + 1)
      if left_depth > right_depth:
          return (left_lca, left_depth)
      elif right_depth > left_depth:
          return (right_lca, right_depth)
      else:
          return (node, left_depth)

  lca_node, _ = dfs(root, 0)
  return lca_node
            