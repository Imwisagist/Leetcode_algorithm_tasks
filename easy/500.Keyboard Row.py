# https://leetcode.com/problems/keyboard-row/

from typing import List

def findWords(words: List[str]) -> List[str]:
    fr, sr, tr, result = "qwertyuiop", "asdfghjkl", "zxcvbnm", []

    for word in words:
        first_char = word[0].lower()

        if first_char in fr:
            chars = fr
        elif first_char in sr:
            chars = sr
        else:
            chars = tr

        for j in word.lower():
            if j not in chars:
                break
        else:
            result.append(word)

    return result


assert findWords(["Hello","Alaska","Dad","Peace"]) == ["Alaska","Dad"]
assert findWords(["adsdf","sfd"]) == ["adsdf","sfd"]
assert findWords(["omk"]) == []
