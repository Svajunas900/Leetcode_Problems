"""110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""Time complexity Big O(n)

Space complexity Big O(n)
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> int:
            return self.height(root) != -1

    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        leftHeight = self.height(node.left)
        
        if leftHeight == -1:
            return -1
        rightHeight = self.height(node.right)
        if rightHeight == -1:
            return -1
            
        if abs(leftHeight - rightHeight) > 1:
            return -1
        
        return max(leftHeight, rightHeight) + 1