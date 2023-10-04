# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description/

from typing import List

def busyStudent(startTime: List[int], endTime: List[int], queryTime: int) -> int:
    return sum(1 for s,e in zip(startTime,endTime) if s <= queryTime <= e)


assert busyStudent([1,2,3],[3,2,7],4) == 1
assert busyStudent([4],[4],4) == 1
