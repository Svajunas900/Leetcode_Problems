"""501. Find Mode in Binary Search Tree


Given the root of a binary search tree (BST) with duplicates, 
return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 
"""


def find_mode(self, root: Optional[TreeNode]) -> list[int]:
    counts = {}
    max_count = 0
    modes = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)

        nonlocal max_count, modes

        counts[node.val] = 1 + counts.get(node.val, 0)

        if counts[node.val] > max_count:
            max_count = counts[node.val]
            modes = [node.val]
        elif counts[node.val] == max_count:
            modes.append(node.val)

        inorder(node.right)

    inorder(root)

    return modes
