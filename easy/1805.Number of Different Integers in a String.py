# https://leetcode.com/problems/number-of-different-integers-in-a-string/description/

def numDifferentIntegers(word: str) -> int:
    res, tmp = [], ""

    for chr in word:
        if chr.isdigit(): tmp += chr
        elif tmp: res.append(tmp); tmp = ""

    if tmp: res.append(tmp)

    return len(set(int(x) for x in res))


assert numDifferentIntegers("a123bc34d8ef34") == 3
assert numDifferentIntegers("leet1234code234") == 2
assert numDifferentIntegers("a1b01c001") == 1
