import pytest
from problem_14 import longestCommonPrefix


test_data_success = [(["flower","flow","flight"], "fl"),
             (["dog","racecar","car"], ""),
             ( ["race","racecar","racoon"], "rac"),
             ]

test_data_failure = [(["flower","flow","flight"], True),
             (["lower","flow","flight"], "fl"),
             ( "MCMXCIV", "fl"),
             ( 241, "True"),
             ]


@pytest.mark.parametrize("nums, expected", test_data_success)
def test_longestCommonPrefix_success(nums, expected):
  assert longestCommonPrefix(nums) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("nums, expected", test_data_failure)
def test_longestCommonPrefix_failure(nums, expected):
  assert longestCommonPrefix(nums) == expected