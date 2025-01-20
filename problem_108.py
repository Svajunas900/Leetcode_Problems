"""108. Convert Sorted Array to Binary Search Tree


Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""

def sortedArrayToBST(self, nums: list) -> Optional[TreeNode]:
  total_nums = len(nums)
  if not total_nums:
      return None
  
  mid_node = total_nums // 2
  return TreeNode(
      nums[mid_node],
      self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node+1:])
  )