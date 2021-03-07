// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	sentinel := &ListNode{Next: head}
	prev := sentinel

	for head != nil && head.Next != nil {
		if head.Val == head.Next.Val {
			// delete next node until next node's value not equals to current node's value
			for head.Next != nil && head.Val == head.Next.Val {
				head.Next = head.Next.Next
			}
			// delete the current node, no need to change pre
			prev.Next = head.Next
		} else {
			// if next node's value not equals to current, just move pre to the next node
			prev = head
		}

		// move to next node
		head = head.Next
	}

	return sentinel.Next
}
