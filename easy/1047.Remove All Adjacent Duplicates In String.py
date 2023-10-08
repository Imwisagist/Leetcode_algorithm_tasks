# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

def removeDuplicates(s: str) -> str:
    res = []

    for chr in s:
        if res and res[-1] == chr: res.pop()
        else: res.append(chr)

    return "".join(res)


assert removeDuplicates("abbaca") == "ca"
assert removeDuplicates("azxxzy") == "ay"