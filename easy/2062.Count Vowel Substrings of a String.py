# https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

def countVowelSubstrings(word: str) -> int:
    vowels, d, result, start = "aeiou", {}, 0, 0

    for idx, char in enumerate(word):
        if char in vowels:

            if not d: start = idx

            d[char] = idx

            if len(d) == 5:
                result += min(d.values()) - start + 1

        elif d: d.clear()
            
    return result


assert countVowelSubstrings("aeiouu") == 2
assert countVowelSubstrings("unicornarihan") == 0
assert countVowelSubstrings("cuaieuouac") == 7
