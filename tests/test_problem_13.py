import unittest
from problem_13 import romanToInt


class RomanToIntTest(unittest.TestCase):
    def test_success(self):
        self.assertEqual(romanToInt("MCCIV"), 1204)
        self.assertEqual(romanToInt("MCMX"), 1910)
        self.assertEqual(romanToInt("MXCIV"), 1094)

    def test_failure(self):
        self.assertNotEqual(romanToInt("MCCIV") == 191)
        self.assertNotEqual(romanToInt("MCMXCIV") == 1910)
        self.assertNotEqual(romanToInt("MCMX") == 190)
        self.assertNotEqual(romanToInt("MCMXCIV") == 11910)
