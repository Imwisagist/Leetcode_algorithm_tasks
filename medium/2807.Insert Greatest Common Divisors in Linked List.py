# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

from typing import Optional
from math import gcd

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next


def insertGreatestCommonDivisors(head: Optional[ListNode]) -> Optional[ListNode]:
    node = head

    while node.next:
        node.next,node = ListNode(gcd(node.val,node.next.val),node.next),node.next

    return head
