# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head

    prev = head
    cur = head.next
    head.next = None

    while cur.next:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    cur.next = prev

    return head
