# https://leetcode.com/problems/remove-outermost-parentheses/description/

def removeOuterParentheses(s: str) -> str:
    res,cnt = "",0

    for c in s:
        if c == "(" and cnt > 0: res += c
        elif c == ")" and cnt > 1: res += c

        cnt += 1 if c == "(" else -1

    return res


assert removeOuterParentheses("(()())(())") == "()()()"
assert removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
assert removeOuterParentheses("()()") == ""
