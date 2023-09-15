# https://leetcode.com/problems/first-letter-to-appear-twice/description/

def repeatedCharacter(s: str) -> str:
    seen: set = set()

    for i in s:
        if i in seen:
            return i
        seen.add(i)


assert repeatedCharacter("abccbaacz") == "c"
assert repeatedCharacter("abcdd") == "d"
