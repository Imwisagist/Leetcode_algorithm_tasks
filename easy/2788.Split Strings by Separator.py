# https://leetcode.com/problems/split-strings-by-separator/description/

from typing import List

def splitWordsBySeparator(words: List[str], separator: str) -> List[str]:
    return [w for word in words for w in word.split(separator) if w]


assert splitWordsBySeparator(["one.two.three","four.five","six"],".") == ["one","two","three","four","five","six"]
assert splitWordsBySeparator(["$easy$","$problem$"],"$") == ["easy","problem"]
assert splitWordsBySeparator(["|||"],"|") == []
