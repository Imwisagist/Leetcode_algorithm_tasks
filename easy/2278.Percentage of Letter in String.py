# https://leetcode.com/problems/percentage-of-letter-in-string/description/

def percentageLetter(s: str, letter: str) -> int:
    return int(s.count(letter) / len(s) * 100)


assert percentageLetter("foobar","o") == 33
assert percentageLetter("jjjj","k") == 0
