# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head: return None

    cur: ListNode = head

    while cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return head


h = d = ListNode(1)
h.next = ListNode(1)
h = h.next
h.next = ListNode(2)
h = h.next
h.next = ListNode(3)
h = h.next
h.next = ListNode(3)

deleteDuplicates(d)
