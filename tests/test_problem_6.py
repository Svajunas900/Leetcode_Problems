import pytest
from problem_6 import convert


test_data_success = [("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
             ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
             ("A", 1, "A")
             ]

test_data_failure = [("PAYPALISHIRING", 4, "PINALSSDIGYAHRPI"),
             ("PAYPALISHIRING", 3, "PAHNAPGELSIIGYIR"),
             ("A", 1, "AAS")
             ]


@pytest.mark.parametrize("s, numRows, expected", test_data_success)
def test_convert_success(s, numRows, expected):
  assert convert(s, numRows) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("s, numRows, expected", test_data_failure)
def test_convert_failure(s, numRows, expected):
  assert convert(s, numRows) == expected
  