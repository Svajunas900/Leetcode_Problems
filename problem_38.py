"""38. Count and Say


The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works 
by replacing consecutive identical characters (repeated 2 or more times) 
with the concatenation of the character and the number marking the count of the characters 
(length of the run). For example, to compress the string "3322251" we replace "33" with "23", 
replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.
"""


def countAndSay(self, n: int) -> str:
    def recursion(x, times):
        if times == n:
            return x
        string = x[0]
        count = 1
        answer = ""
        for i in range(1, len(x)):
            if x[i] == string[0]:
                count += 1
            else:
                answer += str(count)+string
                string = x[i]
                count = 1
        answer += str(count)+string
        return recursion(answer, times+1)
    return recursion("1", 1)

#  def countAndSay(self, n: int) -> str:
#         if n == 1:
#             return "1"
#         def _helper(string):
#             prev = string[0]
#             counter = 1
#             result = []
#             for i in range(1, len(string)):
#                 curr = string[i]
#                 if prev == curr:
#                     counter += 1
#                 else:
#                     result.append(str(counter)+prev)
#                     counter = 1
#                 prev = curr
#             result.append(str(counter)+prev)
#             return "".join(result)
#         ans = "1"
#         for i in range(1,n):
#             ans = _helper(ans)
#         return ans
