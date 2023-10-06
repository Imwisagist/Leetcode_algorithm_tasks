# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

from typing import List

def replaceElements(arr: List[int]) -> List[int]:
    max = -1

    for i in range(len(arr)-1,-1,-1):
        digit = arr[i]; arr[i] = max

        if digit > max: max = digit

    return arr


assert replaceElements([17,18,5,4,6,1]) == [18,6,6,6,1,-1]
assert replaceElements([400]) == [-1]
