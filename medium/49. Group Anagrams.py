# https://leetcode.com/problems/group-anagrams/
from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    d = defaultdict(list)

    for word in strs: d[str(sorted(word))].append(word)

    return list(d.values())


assert groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["a"]) == [["a"]]
