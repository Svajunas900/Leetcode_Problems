# Leetcode_Problems
## Description
Repository consists of [https://leetcode.com/problemset/] problems.
These problems are solved using most popular algorithms and datastructures in python and some of them in javascript.
Some problems have Big O notation for memory and space complexity 

## Example of test cases

```
test_data_success = [("babad", "aba"),
             ("cbbd", "bb"),
             ( "pwwkew", "ww"),
             ]

test_data_failure = [("aasdbcabcbb", 3),
             ("abcasdabcbb", "swrd"),
             ( "abasdcabcbb", True),
             ( "abcasaasdbcbb", "no"),
             ]


@pytest.mark.parametrize("nums, expected", test_data_success)
def test_longestPalindrome_success(nums, expected):
  assert longestPalindrome(nums) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("nums, expected", test_data_failure)
def test_longestPalindrome_failure(nums, expected):
  assert longestPalindrome(nums) == expected
```
