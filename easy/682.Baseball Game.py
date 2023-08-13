# https://leetcode.com/problems/baseball-game/

from typing import List

def calPoints(operations: List[str]) -> int:
    result: list = []

    for char in operations:
        if char in "CD+":
            if char == "C":
                result.pop()
            elif char == "D":
                result.append(result[-1] * 2)
            else:
                result.append(result[-2] + result[-1])
        else:
            result.append(int(char))

    return sum(result)


assert calPoints(["5","2","C","D","+"]) == 30
assert calPoints(["5","-2","4","C","D","9","+","+"]) == 27
assert calPoints(["1","C"]) == 0
