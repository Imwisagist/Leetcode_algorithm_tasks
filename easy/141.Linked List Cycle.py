# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# def hasCycle(head: Optional[ListNode]) -> bool:
# num = 100001 Альтернативное решение
#
#         while head:
#             if head.val > 100000: return True
#
#             head.val = num
#             head = head.next
#
#         return False
