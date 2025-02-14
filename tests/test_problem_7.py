import pytest
from problem_7 import reverse


test_data_success = [(122, 221),
             (311, 113),
             ( 3241, 1423),
             ( 241, 142),
             ]

test_data_failure = [(122, True),
             (311, "bb"),
             ( 3241, 3212),
             ( 241, -321),
             ]


@pytest.mark.parametrize("nums, expected", test_data_success)
def test_reverse_success(nums, expected):
  assert reverse(nums) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("nums, expected", test_data_failure)
def test_reverse_failure(nums, expected):
  assert reverse(nums) == expected