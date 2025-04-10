"""1448. Count Good Nodes in Binary Tree


Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

def goodNodes(root: TreeNode) -> int:
    good = 0

    def dfs(root, mx):
        nonlocal good
        if not root:
            return None
        if root.val >= mx:
            mx = root.val
            good += 1
        dfs(root.left, mx)
        dfs(root.right, mx)
        return good
    return dfs(root, -inf)