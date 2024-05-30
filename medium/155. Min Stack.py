# https://leetcode.com/problems/min-stack/description/


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: self.stack += [val, val]
        else: self.stack += [min(val, self.stack[-2]), val]

    def pop(self) -> None:
        del self.stack[-1]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[-2]
