# https://leetcode.com/problems/longest-uncommon-subsequence-i/

def findLUSlength(a: str, b: str) -> int:
    if a == b: return -1
    else: return max(len(a), len(b))


assert findLUSlength("aba", "cdc") == 3
assert findLUSlength("aaa", "bbb") == 3
assert findLUSlength("aaa", "aaa") == -1
