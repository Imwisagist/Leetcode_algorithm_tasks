# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return self.stack == []


obj = MyStack()

assert obj.empty() is True

obj.push(1)
obj.push(2)

assert obj.top() == 2
assert obj.pop() == 2
assert obj.top() == 1
assert obj.empty() is False
