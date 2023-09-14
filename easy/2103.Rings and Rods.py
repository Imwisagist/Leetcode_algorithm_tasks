# https://leetcode.com/problems/rings-and-rods/description/

def countPoints(rings: str) -> int:
    return sum(1 for i in "0123456789" if "R"+i in rings and "G"+i in rings and "B"+i in rings)


assert countPoints("B0B6G0R6R0R6G9") == 1
assert countPoints("B0R0G0R9R0B0G0") == 1
assert countPoints("G4") == 0
