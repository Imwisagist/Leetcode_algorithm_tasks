# https://leetcode.com/problems/palindrome-number/

def isPalindrome(x: int) -> bool:
	if x < 0 or (x > 0 and x % 10 == 0):
		return False

	result = 0
	while x > result:
		result = result * 10 + x % 10
		x //= 10

	return x == result or x == result // 10


assert isPalindrome(1000021) is False
assert isPalindrome(1200021) is True
