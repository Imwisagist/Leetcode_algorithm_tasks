# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from typing import List

def countCharacters(words: List[str], chars: str) -> int:
    d, count = {}, 0
    d_get = d.get

    for i in chars: d[i] = d_get(i,0) + 1

    for word in words:
        for char in set(word):
            if word.count(char) > d_get(char,0): break
        else: count += len(word)

    return count


assert countCharacters(["cat","bt","hat","tree"],"atach") == 6
assert countCharacters(["hello","world","leetcode"],"welldonehoneyr") == 10
