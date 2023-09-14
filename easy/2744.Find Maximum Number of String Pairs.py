# https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/

from typing import List

def maximumNumberOfStringPairs(words: List[str]) -> int:
    count, seen = 0, set()

    for word in words:
        if word in seen:
            count += 1
        else:
            seen.add(word[::-1])

    return count


assert maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]) == 2
assert maximumNumberOfStringPairs(["ab","ba","cc"]) == 1
assert maximumNumberOfStringPairs(["aa","ab"]) == 0
