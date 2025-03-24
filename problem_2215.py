"""2215. Find the Difference of Two Arrays


Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""

def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
  set_nums1 = set(nums1)
  set_nums2 = set(nums2)
  return [list(set_nums1-set_nums2), list(set_nums2-set_nums1)]