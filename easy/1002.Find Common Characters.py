# https://leetcode.com/problems/find-common-characters/description/

from typing import List

def commonChars(words: List[str]) -> List[str]:
    d: dict = {}
    d_get = d.get

    for i in words[0]: d[i] = d_get(i,0) + 1

    for word in words:
        for char, freq in d.items():
            if word.count(char) < freq:
                d[char] = word.count(char)

    return [k for k, v in d.items() for _ in range(v)]


assert commonChars(["bella","label","roller"]) == ["e", "l", "l"]
assert commonChars(["cool","lock","cook"]) == ["c","o"]
