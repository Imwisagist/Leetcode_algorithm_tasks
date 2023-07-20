# https://leetcode.com/problems/valid-parentheses/

def isValid(s: str) -> bool:
    open_brackets = []

    for bracket in s:
        if bracket in "({[":
            open_brackets.append(bracket)
        elif bracket in ")}]":
            if not open_brackets:
                return False
            if bracket == ")" and open_brackets[-1] == "("\
                    or bracket == "}" and open_brackets[-1] == "{"\
                    or bracket == "]" and open_brackets[-1] == "[":
                open_brackets.pop()
            else:
                return False
        else:
            return False
    return open_brackets == []


assert isValid("()") is True
assert isValid("()[]{}") is True
assert isValid("(}") is False
assert isValid(")(") is False
