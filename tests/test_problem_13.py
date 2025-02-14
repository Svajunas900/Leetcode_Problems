import pytest
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


@pytest.mark.parametrize("nums, expected", test_data_success)
def test_romanToInt_success(nums, expected):
  assert romanToInt(nums) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("nums, expected", test_data_failure)
def test_romanToInt_failure(nums, expected):
  assert romanToInt(nums) == expected