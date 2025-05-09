import unittest
from problem_14 import longestCommonPrefix


class longestCommonPrefixTest(unittest.TestCase):
    def test_success(self):
        self.assertEqual(longestCommonPrefix(
            ["flower", "flow", "flight"]), "fl")
        self.assertEqual(longestCommonPrefix(["dog", "racecar", "car"]), "")
        self.assertEqual(longestCommonPrefix(
            ["race", "racecar", "racoon"]), "rac")

    def test_failure(self):
        self.assertNotEqual(longestCommonPrefix(
            ["flower", "flow", "flight"]) == [[-1, -1, 2], [-1, 0, 1]])
        self.assertNotEqual(longestCommonPrefix(
            ["race", "racecar", "racoon"]) == "flw")
        self.assertNotEqual(longestCommonPrefix(["flower", "flow", "flight"]) == [
                            [-60, 20, 40], [-40, 20, 20]])
        self.assertNotEqual(longestCommonPrefix(
            ["dog", "racecar", "car"]) == 12)
