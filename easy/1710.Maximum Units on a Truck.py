# https://leetcode.com/problems/maximum-units-on-a-truck/

from typing import List

def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    res = 0; boxTypes.sort(key=lambda x: x[1],reverse=True)

    for cnt,units in boxTypes:
        if truckSize >= cnt: res += cnt * units
        else: res += truckSize * units; break

        truckSize -= cnt

    return res


assert maximumUnits([[1,3],[2,2],[3,1]],4) == 8
assert maximumUnits([[5,10],[2,5],[4,7],[3,9]],10) == 91
