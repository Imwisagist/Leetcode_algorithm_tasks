# https://leetcode.com/problems/number-of-employees-who-met-the-target/description/

from typing import List

def numberOfEmployeesWhoMetTarget(hours: List[int], target: int) -> int:
    cnt = 0

    for h in hours:
        if h >= target: cnt += 1

    return cnt


assert numberOfEmployeesWhoMetTarget([0,1,2,3,4],2) == 3
assert numberOfEmployeesWhoMetTarget([5,1,4,2,2],6) == 0
