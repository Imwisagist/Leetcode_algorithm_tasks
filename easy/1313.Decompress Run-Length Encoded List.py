# https://leetcode.com/problems/decompress-run-length-encoded-list/description/

from typing import List

def decompressRLElist(nums: List[int]) -> List[int]:
    res = []

    for i in range(0,len(nums),2): res += [nums[i+1]] * nums[i]

    return res


assert decompressRLElist([1,2,3,4]) == [2,4,4,4]
assert decompressRLElist([1,1,2,3]) == [1,3,3]
