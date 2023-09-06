# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from typing import List

def uncommonFromSentences(s1: str, s2: str) -> List[str]:
    d1: dict = {}

    for i in s1.split() + s2.split():
        d1[i] = d1.get(i, 0) + 1

    return [k for k,v in d1.items() if v == 1]


assert uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet","sour"]
assert uncommonFromSentences("apple apple", "banana") == ["banana"]
