"""437. Path Sum III

Given the root of a binary tree and an integer targetSum, 
return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, 
but it must go downwards (i.e., traveling only from parent nodes to child nodes). 
"""

def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
  self.result = 0
  cache = {0:1}
  self.dfs(root, targetSum, 0, cache)
  return self.result
    
def dfs(self, root, target, currPathSum, cache):
  if root is None:
      return  
  currPathSum += root.val
  oldPathSum = currPathSum - target
  self.result += cache.get(oldPathSum, 0)
  cache[currPathSum] = cache.get(currPathSum, 0) + 1
  self.dfs(root.left, target, currPathSum, cache)
  self.dfs(root.right, target, currPathSum, cache)
  cache[currPathSum] -= 1