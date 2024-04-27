# https://leetcode.com/problems/top-k-frequent-words/description/
from typing import List
from collections import defaultdict
import heapq


def topKFrequent(words: List[str], k: int):
    d = defaultdict(lambda: (0, ""))

    for word in words: d[word] = (d[word][0] - 1, word)

    return [i[1] for i in heapq.nsmallest(k, list(d.values()))]


assert topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
assert topKFrequent(
    ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"]
