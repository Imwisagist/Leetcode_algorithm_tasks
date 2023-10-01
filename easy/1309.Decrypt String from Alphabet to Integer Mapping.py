# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

from string import ascii_lowercase as al

def freqAlphabets(s: str) -> str:
    res,l,r = [],-1,len(s) - 1

    while l < r:
        if s[r] == "#":
            res.append(al[int(s[r-2:r])-1]); r -= 3
        else: res.append(al[int(s[r])-1]); r -= 1

    return "".join(res[::-1])


assert freqAlphabets("10#11#12") == "jkab"
assert freqAlphabets("1326#") == "acz"
