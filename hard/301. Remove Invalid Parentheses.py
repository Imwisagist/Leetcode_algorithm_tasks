# https://leetcode.com/problems/remove-invalid-parentheses/description/
from typing import List


def removeInvalidParentheses(s: str) -> List[str]:
    res, s1 = [], set()
    s1.add(s)

    def check_valid(s):
        left = right = 0

        for chr in s:
            if chr == "(": left += 1
            elif chr == ")": right += 1
            if right > left: return False

        return left == right

    def dfs():
        nonlocal s1

        for string in s1:
            if check_valid(string): res.append(string)

        if res: return res

        s2 = set()

        for string in s1:
            for i, v in enumerate(string):
                if v in "()": s2.add(string[:i] + string[i + 1:])

        s1 = s2
        dfs()

    dfs()

    return res
