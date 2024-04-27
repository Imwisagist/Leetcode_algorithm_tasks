# https://leetcode.com/problems/valid-parentheses/


def isValid(s: str) -> bool:
    d, stack = {'(': ')', '[': ']', '{': '}'}, []

    for c in s:
        if c in d: stack.append(c)
        else:
            if not stack or d[stack.pop()] != c: return False

    return not stack


assert isValid("()") is True
assert isValid("()[]{}") is True
assert isValid("(}") is False
assert isValid(")(") is False
