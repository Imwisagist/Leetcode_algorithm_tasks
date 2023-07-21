# https://leetcode.com/problems/valid-palindrome/


def isPalindrome(s: str) -> bool:
    j, new_s = -1, ""

    for i in s:
        if i.isalpha():
            new_s += i.lower()

    for i in range(len(new_s) // 2):
        if new_s[i] != new_s[j]:
            return False
        j -= 1

    return True


assert isPalindrome("A man, a plan, a canal: Panama") is True
assert isPalindrome("race a car") is False
assert isPalindrome(" ") is True
assert isPalindrome("a.") is True
