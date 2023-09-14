# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

def checkIfPangram(sentence: str) -> bool:
    return len(set(sentence)) == 26


assert checkIfPangram("thequickbrownfoxjumpsoverthelazydog") is True
assert checkIfPangram("leetcode") is False
