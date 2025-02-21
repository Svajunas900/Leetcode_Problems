"""1261. Find Elements in a Contaminated Binary Tree


Given a binary tree with the following rules:

root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
 
"""


class FindElements:
  def __init__(self, root: Optional[TreeNode]):
      self.values = set()

      def recover(node, val):
          if not node:
              return
          node.val = val
          self.values.add(val)
          recover(node.left, 2*val+1)
          recover(node.right, 2*val+2)

      recover(root, 0)    

  def find(self, target: int) -> bool:
      return target in self.values