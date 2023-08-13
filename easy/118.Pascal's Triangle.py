# https://leetcode.com/problems/pascals-triangle/

from typing import List

def generate(numRows: int) -> List[List[int]]:
    result: list = [[1]]

    for i in range(numRows-1):
        row: list = [1]
        for j in range(i):
            row.append(result[i][j]+result[i][j+1])
        row.append(1)
        result.append(row)

    return result


assert generate(5) == [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
assert generate(1) == [[1]]
