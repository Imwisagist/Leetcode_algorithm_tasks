# https://leetcode.com/problems/remove-invalid-parentheses/description/
from typing import List


def removeInvalidParentheses(s: str) -> List[str]:
    def dfs(s, lo, hi, res, d):
        cnt = 0

        for i in range(hi, len(s)):
            sym = s[i]

            if sym in d: cnt += d[sym]
            if cnt < 0:
                for j in range(lo, i + 1):
                    sym2 = s[j]

                    if (sym2 not in d) or (j > lo and sym2 == s[j - 1]): continue
                    if d[sym2] == -1:
                        s_new = s[:j] + s[j + 1:]
                        dfs(s_new, j, i, res, d)
                return

        s_rev = s[::-1]

        if d[')'] == -1: dfs(s_rev, 0, 0, res, d={'(': -1, ')': 1})
        else: res.append(s_rev)

    res = []
    dfs(s, 0, 0, res, d={'(': 1, ')': -1})

    return res
