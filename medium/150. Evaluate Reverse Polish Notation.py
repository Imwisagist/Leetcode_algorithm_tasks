# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
from typing import List


def evalRPN(tokens: List[str]) -> int:
    operation = {"+": lambda x, y: y + x, "-": lambda x, y: y - x,
                 "*": lambda x, y: y * x, "/": lambda x, y: int(y / x)}
    stack = []

    for chr in tokens:
        if chr in operation: stack.append(operation[chr](stack.pop(), stack.pop()))
        else: stack.append(int(chr))

    return stack.pop()


assert evalRPN(["2", "1", "+", "3", "*"]) == 9
assert evalRPN(["4", "13", "5", "/", "+"]) == 6
assert evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
