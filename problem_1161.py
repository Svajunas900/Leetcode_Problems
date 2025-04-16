"""1161. Maximum Level Sum of a Binary Tree


Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
"""


def maxLevelSum(root: Optional[TreeNode]) -> int:
    queue = [root]
    result = root.val-1
    level = 0
    level_result = 0
    while queue:
        temp = []
        level_sum = 0
        level += 1
        for i in queue:
            if i.left:
                temp.append((i.left))
            if i.right:
                temp.append((i.right))
            level_sum += i.val
        queue = temp.copy()
        if level_sum > result:
            result = level_sum
            level_result = level
    return level_result
