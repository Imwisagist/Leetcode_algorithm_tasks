# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 or not list2: return list1 or list2

    list3 = dummy = ListNode(0)

    while list1 and list2:
        if list1.val < list2.val: list3.next = ListNode(list1.val); list1 = list1.next
        else: list3.next = ListNode(list2.val); list2 = list2.next

        list3 = list3.next

    while list1: list3.next = ListNode(list1.val); list1 = list1.next; list3 = list3.next
    while list2: list3.next = ListNode(list2.val); list2 = list2.next; list3 = list3.next

    return dummy.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

mergeTwoLists(l1, l2)

# My solution has been created on leetcode
