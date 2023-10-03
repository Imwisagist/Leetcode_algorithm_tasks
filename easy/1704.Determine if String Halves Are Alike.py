# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/

def halvesAreAlike(s: str) -> bool:
    vowels,cnt = {'a','e','i','o','u','A','E','I','O','U'},0

    for i in range(len(s)//2):
        if s[i] in vowels: cnt += 1

        if s[-1-i] in vowels: cnt -= 1

    return not cnt


assert halvesAreAlike("book") is True
assert halvesAreAlike("textbook") is False
