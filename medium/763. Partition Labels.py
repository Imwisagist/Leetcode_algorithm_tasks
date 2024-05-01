# https://leetcode.com/problems/partition-labels/description/
from typing import List
from collections import defaultdict


def partitionLabels(s: str) -> List[int]:
    d1, d2, cnt, res = defaultdict(int), defaultdict(int), 0, []

    for chr in s: d2[chr] += 1

    for i, v in enumerate(s):
        d1[v] += 1; cnt += 1

        if d1[v] == d2[v]:
            del d1[v]

            if not d1:
                res.append(cnt); cnt = 0

    if cnt: res.append(cnt)

    return res


assert partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
assert partitionLabels("eccbbbbdec") == [10]
