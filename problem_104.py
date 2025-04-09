"""104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""
"""Time complexity Big O(n)

Space complexity Big O(n)
"""
# DFS Solution
def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

def dfs(self, root, depth):
    if not root:
        return depth
    left = self.dfs(root.left, depth+1)
    right = self.dfs(root.right, depth+1)
    depth = max(left, right)
    return depth

# BFS Solution
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    queue = [root]
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth