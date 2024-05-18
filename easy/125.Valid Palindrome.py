# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s: str) -> bool:
    right, new_s = -1, ""

    for i in s:
        if i.isalnum(): new_s += i.lower()

    for left in range(len(new_s) // 2):
        if new_s[left] != new_s[right]: return False

        right -= 1

    return True


assert isPalindrome("race a car") is False
assert isPalindrome("A man, a plan, a canal: Panama") is True
assert isPalindrome("race a car") is False
assert isPalindrome(" ") is True
assert isPalindrome("a.") is True
