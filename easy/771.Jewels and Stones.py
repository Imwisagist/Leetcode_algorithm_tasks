# https://leetcode.com/problems/jewels-and-stones/

def numJewelsInStones(jewels: str, stones: str) -> int:
    return sum(i in jewels for i in stones)


assert numJewelsInStones("aA", "aAAbbbb") == 3
assert numJewelsInStones("z", "ZZ") == 0
