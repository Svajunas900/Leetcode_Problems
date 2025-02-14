import unittest
from problem_11 import maxArea


class TestThreeSum(unittest.TestCase):
  def test_success(self):
    self.assertEqual(maxArea([1,8,6,2,5,4,8,3,7]), 49)
    self.assertEqual(maxArea([1,6,6,2,5,4,2,3,7]), 42)
    self.assertEqual(maxArea([1,2,6,2,5,4,5,3,7]), 36)

  def test_failure(self):
    self.assertFalse(maxArea([1,8,6,2,5,4,8,3,7]) == 191)
    self.assertFalse(maxArea([1,6,6,2,5,4,2,3,7]) == 1910)
    self.assertFalse(maxArea([1,8,6,2,5,4,8,3,7]) == 190)
    self.assertFalse(maxArea([1,2,6,2,5]) == 11910)