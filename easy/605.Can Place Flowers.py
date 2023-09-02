# https://leetcode.com/problems/can-place-flowers/

from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    count, prev = 0, 0

    for i in flowerbed:
        if i == 1:
            if prev == 1:
                count -= 1
            prev = 1
        else:
            if prev == 1:
                prev = 0
            else:
                count += 1
                prev = 1

    return n <= count


assert canPlaceFlowers([1,0,0,0,1], 1) is True
assert canPlaceFlowers([1,0,0,0,1], 2) is False
assert canPlaceFlowers([1,0,0,0,0,1], 2) is False