"""326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x."""


def isPowerOfThree(self, n: int) -> bool:
  return n > 0 and 3**19 % n == 0  