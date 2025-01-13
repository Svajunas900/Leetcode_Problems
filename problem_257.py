"""257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""

def binaryTreePaths(self, root: Optional[TreeNode]) -> list:
    return self.dfs(root, "")

def dfs(self, root, path):
    if root is None:
        return []
    path += str(root.val)
    if not root.left and not root.right:
        return [path]
    path += "->"
    return self.dfs(root.left, path) + self.dfs(root.right, path)