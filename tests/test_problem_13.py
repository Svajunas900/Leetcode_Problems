import unittest
from problem_13 import romanToInt


test_data_success = [("MCMXCIV", 1994),
             ("MCCIV", 1204),
             ( "MCMX", 1910),
             ( "MXCIV", 1094),
             ]

test_data_failure = [(122, True),
             ("MCMXCIV", "bb"),
             ( "MCMXCIV", 3212),
             ( 241, -321),
             ]


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

