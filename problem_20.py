"""20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def isValid(s: list) -> bool:
    stack = []
    for i in s:
        if i in "{([":
            stack.append(i)
        else:
            if len(stack) != 0:
                p = stack.pop()
                if p == "[" and i == "]":
                    continue
                elif p == "{" and i == "}":
                    continue
                elif p == "(" and i == ")":
                    continue
                else:
                    return False
            else:
                return False
    if len(stack) != 0:
        return False
    return True