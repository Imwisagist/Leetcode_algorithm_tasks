# https://leetcode.com/problems/kth-missing-positive-number/description/

from typing import List

def findKthPositive(arr: List[int], k: int) -> int:
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2; missing = arr[m] - (m + 1)
        
        if missing >= k: r = m - 1
        else: l = m + 1

    return r + k + 1


assert findKthPositive([2,3,4,7,11],5) == 9
assert findKthPositive([1,2,3,4],2) == 6
