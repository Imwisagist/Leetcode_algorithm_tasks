# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(head: ListNode) -> int:
    num = 0

    while head:
        num = num * 2 + head.val; head = head.next

    return num


node = ListNode(1)
node.next = ListNode(0)
node.next.next = ListNode(1)

assert getDecimalValue(node) == 5