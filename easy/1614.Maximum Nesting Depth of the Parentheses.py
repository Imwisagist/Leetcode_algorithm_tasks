# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

def maxDepth(s: str) -> int:
    res = cnt = 0

    for chr in s:
        if chr == "(": cnt += 1
        elif chr == ")":
            res = cnt if cnt > res else res; cnt -= 1

    return res


assert maxDepth("(1+(2*3)+((8)/4))+1") == 3
assert maxDepth("(1)+((2))+(((3)))") == 3
