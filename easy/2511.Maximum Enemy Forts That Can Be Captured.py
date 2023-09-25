# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/description/

from typing import List

def captureForts(forts: List[int]) -> int:
    r = len(forts) - 1; l = res = 0; cur_l = cur_r = -1

    while l <= r or r >= 0:
        left_fort, right_fort = forts[l], forts[r]

        if left_fort == 1: cur_l = 0
        elif left_fort == 0:
            if cur_l >= 0: cur_l += 1
        else: res = max(res, cur_l); cur_l = -1

        if right_fort == 1: cur_r = 0
        elif right_fort == 0:
            if cur_r >= 0: cur_r += 1
        else: res = max(res, cur_r); cur_r = -1

        l += 1; r -= 1

    return res

assert captureForts([1,0,0,-1]) == 2
assert captureForts([-1,-1,1,-1,-1,0]) == 0
assert captureForts([1,0,0,-1,0,0,0,0,1]) == 4
assert captureForts([0,0,1,-1]) == 0
