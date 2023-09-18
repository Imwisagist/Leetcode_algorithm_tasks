# https://leetcode.com/problems/reverse-string-ii/

def reverseStr(s: str, k: int) -> str:
    result: str = ""

    for i in range(0,len(s),2*k):
        result += (s[i:i+k][::-1]) + s[i+k:i+2*k]

    return result


assert reverseStr("abcdefg", 2) == "bacdfeg"
assert reverseStr("abcd", 2) == "bacd"
