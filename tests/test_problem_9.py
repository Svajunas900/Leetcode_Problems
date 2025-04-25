import pytest
from problem_9 import isPalindrome


test_data_success = [(121, True),
                     (311, False),
                     (3241, False),
                     (24142, True),
                     ]

test_data_failure = [(122, True),
                     (311, "bb"),
                     (3241, 3212),
                     (241, -321),
                     ]


@pytest.mark.parametrize("nums, expected", test_data_success)
def test_is_palindrome_success(nums, expected):
    assert isPalindrome(nums) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("nums, expected", test_data_failure)
def test_is_palindrome_failure(nums, expected):
    assert isPalindrome(nums) == expected
