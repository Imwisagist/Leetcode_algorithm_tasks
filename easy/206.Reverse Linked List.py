# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = None, head

    while cur:
        following = cur.next
        cur.next = prev
        prev = cur
        cur = following

    return prev
