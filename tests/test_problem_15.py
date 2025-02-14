import unittest
from problem_15 import threeSum


class TestThreeSum(unittest.TestCase):
  def test_success(self):
    self.assertEqual(threeSum([-1,0,1,2,-1,-4]), [[-1, -1, 2], [-1, 0, 1]])
    self.assertEqual(threeSum([0,1,1, -2, -3]), [[-2, 1, 1]])
    self.assertEqual(threeSum([20,52,22,40,-40,20,-60]), [[-60, 20, 40], [-40, 20, 20]])
    self.assertEqual(threeSum([31,63,32,1,-63, 0]), [[-63, 0, 63], [-63, 31, 32]])

  def test_failure(self):
    self.assertFalse(threeSum([-1,0,1,2,-1,-4]) != [[-1, -1, 2], [-1, 0, 1]])
    self.assertFalse(threeSum([0,1,1, -2, -3]) != [[-2, 1, 1]])
    self.assertFalse(threeSum([20,52,22,40,-40,20,-60]) != [[-60, 20, 40], [-40, 20, 20]])
    self.assertFalse(threeSum([31,63,32,1,-63, 0]) != [[-63, 0, 63], [-63, 31, 32]])

