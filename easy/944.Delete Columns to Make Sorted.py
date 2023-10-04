# https://leetcode.com/problems/delete-columns-to-make-sorted/description/

from typing import List

def minDeletionSize(strs: List[str]) -> int:
    return sum(
        1
        for col in map(list, zip(*strs))
        if col != sorted(col)
    )


assert minDeletionSize(["cba","daf","ghi"]) == 1
assert minDeletionSize(["a","b"]) == 0
assert minDeletionSize(["zyx","wvu","tsr"]) == 3
