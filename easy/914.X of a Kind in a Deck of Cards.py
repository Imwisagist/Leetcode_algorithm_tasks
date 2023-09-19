# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/

from collections import Counter
from functools import reduce
from typing import List
from math import gcd

def hasGroupsSizeX(deck: List[int]) -> bool:
    return reduce(gcd,Counter(deck).values()) != 1


assert hasGroupsSizeX([1,2,3,4,4,3,2,1]) is True
assert hasGroupsSizeX([1,1,1,2,2,2,3,3]) is False
