"""2140. Solving Questions With Brainpower

You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order 
(i.e., starting from question 0) and make a decision whether to solve or skip each question. 
Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri 
questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points 
but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.
"""

def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        dp = [-1] * n
        return self.__helper(0, questions, dp, n)
    
def __helper(self, i: int, questions: list[list[int]], dp: list[int], n: int):
    if i >= n:
        return 0
    if dp[i] != -1:
        return dp[i]
    take = questions[i][0] + self.__helper(i+questions[i][1]+1, questions, dp, n)
    dont = self.__helper(i+1, questions, dp, n)
    dp[i] = max(take, dont)
    return dp[i]