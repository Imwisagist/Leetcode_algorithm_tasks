# https://leetcode.com/problems/backspace-string-compare/description/

def backspaceCompare(s: str, t: str) -> bool:
    first, second = [], []

    for chr in s:
        if chr == "#":
            if first: first.pop()
        else: first.append(chr)

    for chr in t:
        if chr == "#":
            if second: second.pop()
        else: second.append(chr)

    return first == second


assert backspaceCompare("bxj##tw", "bxj###tw") is False
assert backspaceCompare("ab#c", "ad#c") is True
assert backspaceCompare("ab##", "c#d#") is True
assert backspaceCompare("a#c", "b") is False
