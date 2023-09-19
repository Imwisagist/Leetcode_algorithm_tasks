# https://leetcode.com/problems/height-checker/description/

from typing import List

def heightChecker(heights: List[int]) -> int:
    arr = [0] * max(heights)
    
    for n in heights: arr[n-1] += 1

    srted = [i for i,v in enumerate(arr,1) for _ in range(v)]

    return sum(1 for i,v in enumerate(heights) if v != srted[i])


assert heightChecker([1,1,4,2,1,3]) == 3
assert heightChecker([5,1,2,3,4]) == 5
assert heightChecker([1,2,3,4,5]) == 0
