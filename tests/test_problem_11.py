import pytest
from problem_11 import maxArea


test_data_success = [([1,8,6,2,5,4,8,3,7], 49),
             ([1,6,6,2,5,4,2,3,7], 42),
             ( [1,4,3,2,5,4,1,3,7], 28),
             ( [1,2,6,2,5,4,5,3,7], 36),
             ]

test_data_failure = [([1,8,6,2,5,4,8,3,7], True),
             ([1,6,6,2,5,4,2,3,7], 432),
             ( [1,4,3,2,5,4,1,3,7], 228),
             ( [1,2,6,2,5,4,5,3,None], 23),
             ]


@pytest.mark.parametrize("nums, expected", test_data_success)
def test_maxArea_success(nums, expected):
  assert maxArea(nums) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("nums, expected", test_data_failure)
def test_maxArea_failure(nums, expected):
  assert maxArea(nums) == expected