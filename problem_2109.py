""" 2109. Adding Spaces to a String

You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices 
in the original string where spaces will be added. Each space should be inserted before the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', 
which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added."""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""
def addSpaces(s: str, spaces: list) -> str:
    leftPointer = 0
    result = []
    for i in spaces:
        rightPointer = i
        result.append(s[leftPointer:rightPointer])
        leftPointer = rightPointer
    result.append(s[rightPointer:])
    return " ".join(result)