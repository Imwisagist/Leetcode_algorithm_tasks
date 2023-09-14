# https://leetcode.com/problems/merge-similar-items/description/

from typing import List

def mergeSimilarItems(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    counter: dict = {}

    for value, weight in items1 + items2:
        counter[value] = counter.get(value, 0) + weight

    return sorted(counter.items())

assert mergeSimilarItems([[1,1],[4,5],[3,8]], [[3,1],[1,5]]) == [(1,6), (3,9), (4,5)]
