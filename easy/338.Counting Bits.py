# https://leetcode.com/problems/counting-bits/
from typing import List


def countBits(n: int) -> List[int]:
    result = [0]

    for i in range(1, n + 1):
        result.append(result[i // 2] + i % 2)

    return result


assert countBits(2) == [0, 1, 1]
assert countBits(5) == [0, 1, 1, 2, 1, 2]
