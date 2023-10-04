# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/description/

from string import ascii_lowercase as al

def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    table = str.maketrans("abcdefghij","0123456789")

    return (int(firstWord.translate(table)) + 
            int(secondWord.translate(table)) == 
            int(targetWord.translate(table))
    )


assert isSumEqual("acb","cba","cdb") is True
assert isSumEqual("aaa","a","aab") is False
assert isSumEqual("aaa","a","aaaa") is True
