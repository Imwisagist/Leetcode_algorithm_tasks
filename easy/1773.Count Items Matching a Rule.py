# https://leetcode.com/problems/count-items-matching-a-rule/description/

from typing import List

def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    d = {"type":0,"color":1,"name":2}

    return sum(1 for arr in items if arr[d[ruleKey]] == ruleValue)


assert countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],"color","silver") == 1
assert countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],"type","phone") == 2
