"""111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""
def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if None in [root.left, root.right]:
        return max(minDepth(root.left), minDepth(root.right)) + 1
    else:
        return min(minDepth(root.left), minDepth(root.right)) + 1