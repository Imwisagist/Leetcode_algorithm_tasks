# https://leetcode.com/problems/path-crossing/description/

def isPathCrossing(path: str) -> bool:
    y, x = 0, 0
    visited: set = {(y,x)}
    actions: dict = {
        "N":(1,0), "E":(0,1),
        "S":(-1,0), "W":(0,-1),
    }

    for step in path:
        x += actions[step][1]
        y += actions[step][0]

        point: tuple = y, x

        if point in visited: return True
        
        visited.add(point)

    return False


assert isPathCrossing("SN") is True
assert isPathCrossing("NES") is False
assert isPathCrossing("NESWW") is True
