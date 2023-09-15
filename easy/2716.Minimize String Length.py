# https://leetcode.com/problems/minimize-string-length/description/

def minimizedStringLength(s: str) -> int:
    return len(set(s))


assert minimizedStringLength("aaabc") == 3
assert minimizedStringLength("cbbd") == 3
assert minimizedStringLength("dddaaa") == 2
