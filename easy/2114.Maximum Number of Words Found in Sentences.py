# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/

from typing import List

def mostWordsFound(sentences: List[str]) -> int:
    res = 0

    for sentence in sentences:
        spaces = sentence.count(" ")

        if spaces > res: res = spaces

    return res + 1


assert mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]) == 6
assert mostWordsFound(["please wait", "continue to fight", "continue to win"]) == 3
