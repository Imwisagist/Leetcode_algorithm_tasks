# https://leetcode.com/problems/unique-number-of-occurrences/description/

from typing import List

def uniqueOccurrences(arr: List[int]) -> bool:
    counter: dict = {}

    for i in arr: counter[i] = counter.get(i,0) + 1

    return len(set(counter.values())) == len(set(arr))


assert uniqueOccurrences([1,2,2,1,1,3]) is True
assert uniqueOccurrences([1,2]) is False
assert uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) is True
