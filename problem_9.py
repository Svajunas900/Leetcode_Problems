"""9. Palindrome Number

Given an integer x, return true if x is a palindrome, 
and false otherwise.
"""


"""Time complexity Big O(log(n))
loop iterates through all x in the reverse order and concatenates string
loop complexity O(log(n))

Space complexity Big O(log(n))
reverse will be as big as the x input converted to string, making it O(log(n))
"""

def isPalindrome(x: int) -> bool:
    reverse = ""
    a_string = str(x)
    for i in range(len(a_string)-1, -1, -1):
        reverse += a_string[i]
    return reverse == a_string