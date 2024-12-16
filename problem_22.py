"""22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


def generateParenthesis(n):
    parentheses = []
    res = []
    
    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(parentheses))
            return
        if openN < n:
            parentheses.append("(")
            backtrack(openN + 1, closedN)
            parentheses.pop()
        if openN > closedN:
            parentheses.append(")")
            backtrack(openN, closedN + 1)
            parentheses.pop()
            
    backtrack(0, 0)