# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/

from typing import List

def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort(); val = arr[1] - arr[0]

    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] != val: return False

    return True


assert canMakeArithmeticProgression([3,5,1]) is True
assert canMakeArithmeticProgression([1,2,4]) is False
