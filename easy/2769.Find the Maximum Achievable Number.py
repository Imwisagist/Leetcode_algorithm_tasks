# https://leetcode.com/problems/find-the-maximum-achievable-number/description/

def theMaximumAchievableX(num: int, t: int) -> int:
    return num + t * 2


assert theMaximumAchievableX(4,1) == 6
assert theMaximumAchievableX(3,2) == 7
