"""838. Push Dominoes

There are n dominoes in a line, and we place each domino vertically upright. 
In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. 
Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, 
it stays still due to the balance of the forces.

For the purposes of this question, 
we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.
"""


def pushDominoes(self, dominoes: str) -> str:
    dominoes = 'L' + dominoes + 'R'
    res = ''
    prev = 0
    for curr in range(1, len(dominoes)):
        if dominoes[curr] == '.':
            continue
        span = curr - prev - 1
        if prev > 0:
            res += dominoes[prev]
        if dominoes[prev] == dominoes[curr]:
            res += dominoes[prev] * span
        elif dominoes[prev] == 'L' and dominoes[curr] == 'R':
            res += '.' * span
        else:
            res += 'R' * (span // 2) + '.' * (span % 2) + 'L' * (span // 2)
        prev = curr
    return res
