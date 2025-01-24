"""671. Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value, 
where each node in this tree has exactly two or zero sub-node. 
If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. 
More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead."""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
  def dfs(root, ans):
      if not root:
          return

      if root.val < ans[1] and root.val > ans[0]:
          ans[1] = root.val
      else:
          ans[0] = min(ans[0], root.val)

      dfs(root.left, ans)
      dfs(root.right, ans)

  ans = [inf, inf]
  dfs(root, ans)
  return ans[1] if ans[1] != inf else -1