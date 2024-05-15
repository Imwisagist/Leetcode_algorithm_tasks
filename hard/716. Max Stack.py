from heapq import heappush, heappop
# from sortedcontainers import SortedList

# class MaxStack:
#
#     def __init__(self):
#         self.stack = SortedList()
#         self.values = SortedList()
#         self.cnt = 0
#
#     def push(self, x: int) -> None:
#         self.stack.add((self.cnt, x))
#         self.values.add((x, self.cnt))
#         self.cnt += 1
#
#     def pop(self) -> int:
#         idx, val = self.stack.pop()
#         self.values.remove((val, idx))
#         return val
#
#     def top(self) -> int:
#         return self.stack[-1][1]
#
#     def peekMax(self) -> int:
#         return self.values[-1][0]
#
#     def popMax(self) -> int:
#         val, idx = self.values.pop()
#         self.stack.remove((idx, val))
#         return val


class MaxStack:

    def __init__(self):
        self.stack = []
        self.minHeap = []
        self.idx = 0
        self.removed = set()

    def push(self, x: int) -> None:
        self.stack.append((x, self.idx))
        heappush(self.minHeap, (-x, -self.idx))
        self.idx += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed: self.stack.pop()

        val, i = self.stack.pop()
        self.removed.add(i)

        return val

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed: self.stack.pop()

        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.minHeap and -self.minHeap[0][1] in self.removed: heappop(self.minHeap)

        return -self.minHeap[0][0]

    def popMax(self) -> int:
        while self.minHeap and -self.minHeap[0][1] in self.removed: heappop(self.minHeap)

        val, i = heappop(self.minHeap)
        self.removed.add(-i)

        return -val
