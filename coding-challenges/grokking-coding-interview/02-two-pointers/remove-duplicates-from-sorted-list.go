// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	current := head

	for current != nil {
		if current.Next != nil && current.Val == current.Next.Val {
			current.Next = current.Next.Next
			continue
		}

		current = current.Next
	}

	return head
}
