"""101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
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

def isSymmetric(root: Optional[TreeNode]) -> bool:
    """Checking if root exists if exists call isMirror"""
    if not root:
        return True
    return isMirror(root.left,  root.right)

def isMirror(self, subTreeLeft: Optional[TreeNode], subTreeRight: Optional[TreeNode]) -> bool:
    """Base Case
    Checking if both is None
    """
    if subTreeLeft is None and subTreeRight is None:
        return True
    """Checking if one of them is None"""
    if subTreeLeft is None or subTreeRight is None:
        return False
    """Checking if values are equal"""
    if subTreeLeft.val == subTreeRight.val:
        return self.isMirror(subTreeLeft.left, subTreeRight.right) and self.isMirror(subTreeLeft.right, subTreeRight.left)      
    return False