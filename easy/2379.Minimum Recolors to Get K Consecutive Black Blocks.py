# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

def minimumRecolors(blocks: str, k: int) -> int:
    res = k

    for i in range(len(blocks)+1-k):
        res = min(res,k-blocks[i:i+k].count("B"))

    return 0 if res <= 0 else res


assert minimumRecolors("WBBWWBBWBW",7) == 3
assert minimumRecolors("WBWBBBW",2) == 0
