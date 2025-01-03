"""145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root) -> list:
    if root is None:
        return []
    res = []
    return traverse(root, res)
    

def traverse(node, res):
    if node is None:
        return 
    if node.left:
        traverse(node.left, res)
    if node.right:
        traverse(node.right, res)
    res.append(node.val)
    return res

