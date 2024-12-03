"""9. Palindrome Number

Given an integer x, return true if x is a palindrome, 
and false otherwise.
"""


def isPalindrome(x):
    reverse = ""
    a_string = str(x)
    for i in range(len(a_string)-1, -1, -1):
        reverse += a_string[i]
    return reverse == a_string