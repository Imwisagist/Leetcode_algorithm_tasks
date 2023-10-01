# https://leetcode.com/problems/replace-all-digits-with-characters/description/

from string import ascii_lowercase as al

def replaceDigits(s: str) -> str:
    res,n = "",len(s)

    for i in range(1,n,2):
        res += s[i-1] + al[al.index(s[i-1])+int(s[i])]

    return res if n % 2 == 0 else res + s[-1]

assert replaceDigits("a1b2c3d4e") == "abbdcfdhe"
assert replaceDigits("a1c1e1") == "abcdef"
assert replaceDigits("a1b2c3d4e") == "abbdcfdhe"
