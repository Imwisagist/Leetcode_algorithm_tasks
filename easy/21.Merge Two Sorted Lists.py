# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1: return list2
    if not list2: return list1

    if list1.val < list2.val:
        master = dummy = list1
        slave = list2
    else:
        master = dummy = list2
        slave = list1

    while slave:
        master_next = master.next
        if master.val <= slave.val and (master_next is None or master_next.val >= slave.val):
            master.next = slave
            saved_slave_next = slave.next
            slave.next = master_next
            slave = saved_slave_next
            master = master.next
        else:
            master = master.next

    return dummy


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

mergeTwoLists(l1, l2)

# My solution has been created on leetcode
