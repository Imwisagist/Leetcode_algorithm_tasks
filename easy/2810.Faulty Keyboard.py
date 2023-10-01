# https://leetcode.com/problems/faulty-keyboard/description/

def finalString(s: str) -> str:
    res = ""

    for chr in s:
        if chr == "i": res = res[::-1]
        else: res += chr

    return res


assert finalString("string") == "rtsng"
assert finalString("poiinter") == "ponter"
