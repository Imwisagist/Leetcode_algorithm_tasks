# https://leetcode.com/problems/reverse-words-in-a-string-iii/

def reverseWords(s: str) -> str:
    return " ".join(x[::-1] for x in s.split())


assert reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert reverseWords("God Ding") == "doG gniD"
