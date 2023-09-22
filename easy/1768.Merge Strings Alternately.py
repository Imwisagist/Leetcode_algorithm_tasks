# https://leetcode.com/problems/merge-strings-alternately/

def mergeAlternately(word1: str, word2: str) -> str:
    l1, l2, res = len(word1), len(word2), []; l = r = 0

    while l < l1 and r < l2:
        res += [word1[l], word2[r]]; l += 1; r += 1

    res += word1[l:] if l1 >= l2 else word2[l:]

    return "".join(res)


assert mergeAlternately("abc","pqr") == "apbqcr"
assert mergeAlternately("ab","pqrs") == "apbqrs"
assert mergeAlternately("abcd","pq") == "apbqcd"
