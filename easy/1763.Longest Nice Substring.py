# https://leetcode.com/problems/longest-nice-substring/description/

def longestNiceSubstring(s: str) -> str:
    result, stack = "", [s]

    while stack:
        word = stack.pop()

        if not word: continue
        
        uniq_chrs = set(list(word))
        
        for idx, val in enumerate(word):
            if val.swapcase() not in uniq_chrs:
                stack.append(word[idx+1:])
                stack.append(word[:idx])
                break
        else:
            result = max(result, word, key=len)

    return result


assert longestNiceSubstring("YazaAay") == "aAa"
assert longestNiceSubstring("Bb") == "Bb"
assert longestNiceSubstring("c") == ""
