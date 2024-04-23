# https://leetcode.com/problems/generate-parentheses/
from typing import List


def generateParenthesis(n: int) -> List[str]:
    res = []

    def dfs(l, r, comb):
        if len(comb) == 2 * n:
            res.append(comb)
            return
        if l < n: dfs(l + 1, r, comb + "(")
        if r < l: dfs(l, r + 1, comb + ")")

    dfs(0, 0, "")

    return res


assert generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
assert generateParenthesis(1) == ["()"]
