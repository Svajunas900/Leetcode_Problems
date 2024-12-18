"""125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


def isPalindrome(s):
    clean_text = "".join(char for char in s if char.isalnum())
    clean_text = clean_text.lower()
    if len(clean_text) == 0:
        return True
    start = 0
    end = len(clean_text)-1
    for _ in range(len(clean_text)//2):
        if clean_text[start] != clean_text[end]:
            return False
        start += 1
        end -= 1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))