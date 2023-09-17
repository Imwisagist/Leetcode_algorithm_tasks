# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/

from collections import Counter
from typing import List

def makeEqual(words: List[str]) -> bool:
    word_count, char_count = len(words), Counter()
    
    for word in words: char_count.update(word)

    return not any(val % word_count != 0 for val in char_count.values())


assert makeEqual(["abc","aabc","bc"]) is True
assert makeEqual(["ab","a"]) is False