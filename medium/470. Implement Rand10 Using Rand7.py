# https://leetcode.com/problems/implement-rand10-using-rand7/description/


class Solution:
    n = 0

    def rand10(self):
        """
        :rtype: int
        """
        self.n += 1

        return self.n % 10 + 1
