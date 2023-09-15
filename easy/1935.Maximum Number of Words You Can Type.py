# https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/

def canBeTypedWords(text: str, brokenLetters: str) -> int:
    counter: int = 0

    for word in text.split():
        for char in word:
            if char in brokenLetters:
                break
        else:
            counter += 1

    return counter


assert canBeTypedWords("hello world", "ad") == 1
assert canBeTypedWords("leet code", "lt") == 1
assert canBeTypedWords("leet code", "e") == 0
