class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def inorderTraversal(root) -> list:
  return traverse(root)

def traverse(root):
    if root is None:
        return
    if root.left:
        traverse(root.left)
        print(root.val)
    if root.right:
        traverse(root.right)
        print(root.val)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node2.right = node3

print(inorderTraversal(node1))