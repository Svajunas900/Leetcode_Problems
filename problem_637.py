"""637. Average of Levels in Binary Tree

Given the root of a binary tree, 
return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.
"""

"""Time complexity Big O(n)
Time complexity depends on how much nodes are in the tree 

Space complexity Big O(n)
Space as well
"""

def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
  q, ans = [root], []
  while len(q):
      qlen, row = len(q), 0
      for i in range(qlen):
          curr = q.pop(0)
          row += curr.val
          if curr.left: 
              q.append(curr.left)
          if curr.right:
              q.append(curr.right)
      ans.append(row/qlen)
  return ans