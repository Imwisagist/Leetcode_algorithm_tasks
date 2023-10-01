# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

from typing import List

def finalValueAfterOperations(operations: List[str]) -> int:
    op_dict = {"--X" : -1, "X--" : -1, "++X" : 1, "X++" : 1}

    return sum(op_dict[o] for o in operations)


assert finalValueAfterOperations(["--X","X++","X++"]) == 1
assert finalValueAfterOperations(["++X","++X","X++"]) == 3
assert finalValueAfterOperations(["X++","++X","--X","X--"]) == 0
