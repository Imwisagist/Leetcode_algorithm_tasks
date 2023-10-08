# https://leetcode.com/problems/minimum-absolute-difference/description/

from typing import List

def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    arr.sort(); res,m = [],float("inf")

    for i in range(1,len(arr)): m = min(m,arr[i]-arr[i-1])

    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] == m: res.append([arr[i-1],arr[i]])

    return res


assert minimumAbsDifference([4,2,1,3]) == [[1,2],[2,3],[3,4]]
assert minimumAbsDifference([1,3,6,10,15]) == [[1,3]]
assert minimumAbsDifference([3,8,-10,23,19,-4,-14,27]) == [[-14,-10],[19,23],[23,27]]
