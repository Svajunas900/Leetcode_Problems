""" 144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""

def preorderTraversal(root: Optional[TreeNode]) -> list:
    res = []
    if not root:
        return res
    return dfs(root, res)

def dfs(self, root, res):
    if not root:
        return res
    res.append(root.val)
    if root.left:
        self.dfs(root.left, res)
    if root.right:
        self.dfs(root.right, res)
    return res