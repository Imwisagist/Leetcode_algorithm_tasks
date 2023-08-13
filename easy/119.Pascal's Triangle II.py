# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List

def getRow(rowIndex: int) -> List[int]:
    result: list = [[1]]

    for i in range(rowIndex):
        row: list = [1]
        for j in range(i):
            row.append(result[i][j]+result[i][j+1])
        row.append(1)
        result.append(row)

    return result[-1]


assert getRow(3) == [1,3,3,1]
assert getRow(0) == [1]
assert getRow(1) == [1,1]
