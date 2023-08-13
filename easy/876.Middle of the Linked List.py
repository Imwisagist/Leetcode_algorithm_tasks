# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    nothead, lenght = head, 1

    while nothead.next:
        nothead = nothead.next
        lenght += 1

    lenght //= 2

    while lenght > 0:
        head = head.next
        lenght -= 1

    return head
