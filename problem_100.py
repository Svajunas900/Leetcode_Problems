"""100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Base Case 
    Checking if both Tree Nodes are None, if they are return True """
    if p is None and q is None:
        return True
    """Checking if one of the Tree Nodes is None, if it is return False"""
    if p is None or q is None:
        return False
    """Checking the value of Nodes"""
    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return False