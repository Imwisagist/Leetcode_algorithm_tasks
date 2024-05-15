# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    if not head: return True

    slow = fast = head
    prev = None

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    while slow:
        curr = slow
        slow = slow.next
        curr.next = prev
        prev = curr

    while prev:
        if prev.val != head.val: return False

        prev = prev.next
        head = head.next
    
    return True


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(1)

assert isPalindrome(l1) is True

l2 = ListNode(1)
l2.next = ListNode(2)

assert isPalindrome(l2) is False
