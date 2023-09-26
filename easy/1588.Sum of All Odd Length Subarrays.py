# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/

from typing import List

def sumOddLengthSubarrays(arr: List[int]) -> int:
    n = len(arr)

    return sum(
        sum(arr[l:r]) 
        for l in range(n) 
        for r in range(l+1, n+1, 2)
    )


assert sumOddLengthSubarrays([1,4,2,5,3]) == 58
assert sumOddLengthSubarrays([1,2]) == 3
assert sumOddLengthSubarrays([10,11,12]) == 66
