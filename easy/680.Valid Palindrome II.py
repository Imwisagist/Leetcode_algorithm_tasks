# https://leetcode.com/problems/valid-palindrome-ii/

def validPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            s1, s2 = s[l:r], s[l+1:r+1]

            return s1 == s1[::-1] or s2 == s2[::-1]

        l += 1; r -= 1

    return True


assert validPalindrome("aba") is True
assert validPalindrome("abcderfafredcxba") is True
assert validPalindrome("ebcbbececabbacecbbcbe") is True
assert validPalindrome("lcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucul") is True
