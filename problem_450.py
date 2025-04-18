"""450. Delete Node in a BST

Given a root node reference of a BST and a key, 
delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
"""


def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return root
    if root.val > key:
        root.left = self.deleteNode(root.left, key)
    elif root.val < key:
        root.right = self.deleteNode(root.right, key)
    else:
        if not root.left and not root.right:
            return None
        elif not root.left or not root.right:
            return root.left if root.left else root.right
        else:
            successor = self._get_min(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

    return root


def _get_min(self, node: TreeNode) -> TreeNode:
    while node.left:
        node = node.left
    return node
