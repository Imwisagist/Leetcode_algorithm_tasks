# https://leetcode.com/problems/flipping-an-image/

from typing import List

def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    n, invert = len(image) - 1, (1,0)

    if n % 2 == 0: invert_mid = True
    else: invert_mid = False

    for arr in image:
        l, r = 0, n
        
        if invert_mid: arr[n // 2] = invert[arr[n // 2]]

        while l < r:
            arr[l], arr[r] = invert[arr[r]], invert[arr[l]]
            l += 1; r -= 1

    return image

assert flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]
assert flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
