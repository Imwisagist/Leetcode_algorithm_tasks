# https://leetcode.com/problems/valid-palindrome-ii/

def validPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            s1 = s[:left] + s[left+1:]
            s2 = s[:right] + s[right+1:]

            if s1 == s1[::-1]: return True
            elif s2 == s2[::-1]: return True
            else: return False

        left += 1
        right -= 1

    return True


assert validPalindrome("aba") is True
assert validPalindrome("abcderfafredcxba") is True
assert validPalindrome("ebcbbececabbacecbbcbe") is True
assert validPalindrome("lcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucul") is True
