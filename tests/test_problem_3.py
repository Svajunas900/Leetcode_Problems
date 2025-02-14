import pytest
from problem_3 import lengthOfLongestSubstring


test_data_success = [("abcabcbb", 3),
             ("bbbbb", 1),
             ( "pwwkew", 3),
             ]

test_data_failure = [("aasdbcabcbb", 3),
             ("abcasdabcbb", 3),
             ( "abasdcabcbb", 3),
             ( "abcasaasdbcbb", 3),
             ]


@pytest.mark.parametrize("nums, expected", test_data_success)
def test_lengthOfLongestSubstring_success(nums, expected):
  assert lengthOfLongestSubstring(nums) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("nums, expected", test_data_failure)
def test_lengthOfLongestSubstring_failure(nums, expected):
  assert lengthOfLongestSubstring(nums) == expected
  