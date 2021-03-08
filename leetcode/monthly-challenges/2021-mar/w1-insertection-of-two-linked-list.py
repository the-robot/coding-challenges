# https://leetcode.com/problems/intersection-of-two-linked-lists/

"""
Topic: Linked List
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cache = set()
        while headA:
            cache.add(headA)
            headA = headA.next
        
        while headB:
            if headB in cache:
                return headB
            headB = headB.next
        
        return None
