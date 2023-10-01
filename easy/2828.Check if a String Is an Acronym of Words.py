# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/

from typing import List

def isAcronym(words: List[str], s: str) -> bool:
    return "".join(w[0] for w in words) == s


assert isAcronym(["alice","bob","charlie"],"abc") is True
assert isAcronym(["an","apple"],"a") is False
assert isAcronym(["never","gonna","give","up","on","you"],"ngguoy") is True
