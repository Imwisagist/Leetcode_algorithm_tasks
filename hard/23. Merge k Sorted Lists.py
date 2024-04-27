# https://leetcode.com/problems/merge-k-sorted-lists/description/
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    h = []
    head = cur = ListNode(0)

    for i in range(len(lists)):
        if lists[i]: heapq.heappush(h, (lists[i].val, i, lists[i]))

    while h:
        node = heapq.heappop(h)[2]
        cur.next = node
        cur = cur.next

        if node.next:
            i += 1
            heapq.heappush(h, (node.next.val, i, node.next))

    return head.next
