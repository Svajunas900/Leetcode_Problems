import unittest
from problem_13 import romanToInt


class TestThreeSum(unittest.TestCase):
  def test_success(self):
    self.assertEqual(romanToInt("MCCIV"), 1204)
    self.assertEqual(romanToInt("MCMX"), 1910)
    self.assertEqual(romanToInt("MXCIV"), 1094)

  def test_failure(self):
    self.assertFalse(romanToInt("MCCIV") == 191)
    self.assertFalse(romanToInt("MCMXCIV") == 1910)
    self.assertFalse(romanToInt("MCMX") == 190)
    self.assertFalse(romanToInt("MCMXCIV") == 11910)

