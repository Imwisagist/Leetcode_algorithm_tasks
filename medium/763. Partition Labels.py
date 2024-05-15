# https://leetcode.com/problems/partition-labels/description/
from typing import List
from collections import defaultdict


def partitionLabels(s: str) -> List[int]:
    d, res = defaultdict(int), []
    l, r = -1, 0

    for i, v in enumerate(s):
        d[v] = i

    for i, v in enumerate(s):
        r = max(d[v], r)

        if r == i:
            res.append(r - l)
            l = r

    return res


assert partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
assert partitionLabels("eccbbbbdec") == [10]
