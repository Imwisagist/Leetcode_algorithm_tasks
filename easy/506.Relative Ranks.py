# https://leetcode.com/problems/relative-ranks/

from typing import List

def findRelativeRanks(score: List[int]) -> List[str]:
    sorted_scores, ranks = sorted(score, reverse=True), {}

    for i, s in enumerate(sorted_scores):
        if i >= 3:
            ranks[s] = str(i + 1)
        elif i == 1:
            ranks[s] = "Silver Medal"
        elif i == 2:
            ranks[s] = "Bronze Medal"
        else:
            ranks[s] = "Gold Medal"

    return [ranks[s] for s in score]


assert findRelativeRanks([5,4,3,2,1]) == ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
assert findRelativeRanks([10,3,8,9,4]) == ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
