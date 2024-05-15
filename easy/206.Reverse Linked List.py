# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None

    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev

    # def dfs(prev, cur):
    #     if not cur: return prev
    #
    #     next = cur.next
    #     cur.next = prev
    #
    #     return dfs(cur, next)
    #
    # return dfs(None, head)
