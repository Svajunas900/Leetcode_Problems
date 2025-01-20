"""112. Path Sum

Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""Time complexity Big O(n)

Space complexity Big O(n)
"""

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.val
    
    left_sum = hasPathSum(root.left, targetSum-root.val)
    right_sum = hasPathSum(root.right, targetSum-root.val)
    return left_sum or right_sum