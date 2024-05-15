# https://leetcode.com/problems/min-stack/description/


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        prev = self.stack[-1][1] if self.stack else val
        self.stack.append((val, val if val < prev else prev))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
