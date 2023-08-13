# https://leetcode.com/problems/valid-perfect-square/

def isPerfectSquare(num: int) -> bool:
        left, right = 1, num

        while left <= right:
            mid: int = (left + right) // 2
            square: int = mid * mid
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1

        return False


assert isPerfectSquare(16) is True
assert isPerfectSquare(14) is False
