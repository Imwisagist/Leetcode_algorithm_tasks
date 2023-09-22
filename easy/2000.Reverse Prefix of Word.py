# https://leetcode.com/problems/reverse-prefix-of-word/description/

def reversePrefix(word: str, ch: str) -> str:
    n, res = len(word), list(word); l = r = 0

    while r < n:
        if word[r] == ch:
            while l < r:
                res[l], res[r] = res[r], res[l]
                l += 1; r -= 1
            break
        else: r += 1

    return "".join(res)


assert reversePrefix("abcdefd", "d") == "dcbaefd"
assert reversePrefix("xyxzxe", "z") == "zxyxxe"
assert reversePrefix("abcd", "z") == "abcd"
