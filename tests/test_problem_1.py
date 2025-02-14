import pytest
from problem_1 import twoSum


test_data_success = [([1,5,2,4], 3, [2, 0]),
             ([1,4,6,1], 2, [3, 0]),
             ([20,52,22,40], 42, [2, 0]),
             ([31,63,32,1], 63, [2, 0]),
             ]

test_data_failure = [([1,5,2,-4], 2, [2, 0]),
             ([1,4,6,1], 24, [3, 0]),
             ([20,52,22,40], 422, [2, 0]),
             ([31,63,32,1], 623, [2, 0]),
             ]


@pytest.mark.parametrize("nums, target, expected", test_data_success)
def test_twoSum_success(nums, target, expected):
  assert twoSum(nums, target) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("nums, target, expected", test_data_failure)
def test_twoSum_failure(nums, target, expected):
  assert twoSum(nums, target) == expected
  