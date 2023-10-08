# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

from typing import List
from collections import Counter

def countStudents(students: List[int], sandwiches: List[int]) -> int:
    stu = Counter(students)

    for san in sandwiches:
        if stu[san]: stu[san] -= 1
        else: return stu[1] + stu[0]

    return 0


assert countStudents([1,1,0,0],[0,1,0,1]) == 0
assert countStudents([1,1,1,0,0,1],[1,0,0,0,1,1]) == 3
