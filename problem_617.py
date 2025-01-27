"""617. Merge Two Binary Trees


You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, 
some nodes of the two trees are overlapped while the others are not. 
You need to merge the two trees into a new binary tree. 
The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. 
Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
"""

"""Time complexity Big O(n)
Space complexity Big O(n)

"""

def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
  if not root1 and not root2: return None
  answer = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
  answer.left = self.mergeTrees(root1 and root1.left, root2 and root2.left)
  answer.right = self.mergeTrees(root1 and root1.right, root2 and root2.right)
  return answer