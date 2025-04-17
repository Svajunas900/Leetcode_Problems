"""700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.
"""


def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root == None or root.val == val:
        return root
    return self.searchBST(root.right, val) if root.val < val else self.searchBST(root.left, val)
