import pytest
from problem_15 import threeSum


test_data_success = [
             ([-1,0,1,2,-1,-4], [[-1, -1, 2], [-1, 0, 1]]),
             ([0,1,1, -2, -3], [[-2, 1, 1]]),
             ([20,52,22,40,-40,20,-60], [[-60, 20, 40], [-40, 20, 20]]),
             ([31,63,32,1,-63, 0], [[-63, 0, 63], [-63, 31, 32]]),
             ]

test_data_failure = [
             ([-1,0,1,2,-1,-4], []),
             ([1,4,6,1], [3, 0]),
             ([20,52,22,40], [2, 0]),
             ([31,63,32,1], [2, 0]),
             ]


@pytest.mark.parametrize("nums, expected", test_data_success)
def test_threeSum_success(nums, expected):
  assert threeSum(nums) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("nums, expected", test_data_failure)
def test_threeSum_failure(nums, expected):
  assert threeSum(nums) == expected