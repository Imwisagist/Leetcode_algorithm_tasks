# https://leetcode.com/problems/find-the-town-judge/description/

from typing import List

def findJudge(n: int, trust: List[List[int]]) -> int:
    people = [0] * (n+1)

    for who_trust, whom_trust in trust:
        people[who_trust] -= 1; people[whom_trust] += 1

    for i in range(1, n+1):
        if people[i] == n-1: return i
        
    return -1


assert findJudge(2,[[1,2]]) == 2
assert findJudge(3,[[1,3],[2,3]]) == 3
assert findJudge(3,[[1,3],[2,3],[3,1]]) == -1
