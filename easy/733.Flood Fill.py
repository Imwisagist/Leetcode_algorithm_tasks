# https://leetcode.com/problems/flood-fill/

from typing import List

def fill(image, sr, sc, color, cur):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]): return

        if cur != image[sr][sc]: return

        image[sr][sc] = color

        fill(image, sr-1, sc, color, cur)
        fill(image, sr+1, sc, color, cur)
        fill(image, sr, sc-1, color, cur)
        fill(image, sr, sc+1, color, cur)
        
def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc] == color: return image

    fill(image, sr, sc, color, image[sr][sc])

    return image


assert floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
assert floodFill([[0,0,0],[0,0,0]], 0, 0, 0) == [[0,0,0],[0,0,0]]
