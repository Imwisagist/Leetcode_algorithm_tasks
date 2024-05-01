# https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = l3 = ListNode()
    whole_part = 0

    while l1 or l2:
        rest_part = 0

        if l1:
            rest_part += l1.val; l1 = l1.next
        if l2:
            rest_part += l2.val; l2 = l2.next

        rest_part += whole_part; whole_part = 0

        if rest_part > 9: whole_part, rest_part = divmod(rest_part, 10)

        l3.next = ListNode(rest_part); l3 = l3.next

    if whole_part: l3.next = ListNode(whole_part)

    return dummy.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(9)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)

l3 = ListNode(7)
l3.next = ListNode(0)
l3.next.next = ListNode(4)
l3.next.next.next = ListNode(0)
l3.next.next.next.next = ListNode(1)
addTwoNumbers(l1, l2)
