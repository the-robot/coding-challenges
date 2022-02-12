# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minHeap = []

        # store all the numbers in minHeap
        for node in lists:
            while node:
                heapq.heappush(minHeap, node.val)
                node = node.next

        # head is the starting of the node and will be used to return
        head, tail = None, None
        while minHeap:
            val = heapq.heappop(minHeap)
            
            if head is None:
                head = tail = ListNode(val)
            else:
                tail.next = ListNode(val)
                tail = tail.next

        return head
