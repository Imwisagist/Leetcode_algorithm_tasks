# https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(s: str) -> int:
    cnt: int = 0

    for i in range(len(s) - 1,-1,-1):
        if s[i] == " ":
            if cnt:
                return cnt
        else:
            cnt += 1
        
    return cnt


assert lengthOfLastWord("Hello World") == 5
assert lengthOfLastWord("   fly me   to   the moon  ") == 4
assert lengthOfLastWord("luffy is still joyboy") == 6
assert lengthOfLastWord("a ") == 1

# My solution has been created on leetcode
