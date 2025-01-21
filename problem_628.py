"""628. Maximum Product of Three Numbers


Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
"""

def maximumProduct(self, nums: List[int]) -> int:
  nums.sort()
  final_result = 0
  result_1 = nums[0] * nums[1] * nums[2]
  result_2 = nums[0] * nums[1] * nums[-1]
  result_3 = nums[-1] * nums[-2] * nums[-3]
  if result_1 >= result_2 and result_1 >= result_3:
      final_result = result_1
  if result_2 >= result_3 and result_2 >= result_1:
      final_result = result_2
  if result_3 >= result_2 and result_3 >= result_1:
      final_result = result_3
  return final_result