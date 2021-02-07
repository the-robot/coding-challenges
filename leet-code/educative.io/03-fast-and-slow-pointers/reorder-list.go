// https://leetcode.com/problems/reorder-list/description/

package main

// ListNode is a linked list array element
type ListNode struct {
	Val  int
	Next *ListNode
}

func reorderList(head *ListNode) {
	if head == nil || head.Next == nil {
		return
	}

	// find middle of the Linked List
	slow := head
	fast := head

	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}

	// reverse the mid-end I.e.
	// 1 -> 2 -> 3 -> 4 will become
	// 1 -> 2 -> 4 -> 3
	headFirstHalf := head
	headSecondHalf := reverse(slow)

	for headFirstHalf != nil && headSecondHalf != nil {
		temp := headFirstHalf.Next
		headFirstHalf.Next = headSecondHalf
		headFirstHalf = temp

		temp = headSecondHalf.Next
		headSecondHalf.Next = headFirstHalf
		headSecondHalf = temp
	}

	// set the next of the last node to null
	if headFirstHalf != nil {
		headFirstHalf.Next = nil
	}
}

func reverse(head *ListNode) *ListNode {
	var prev *ListNode = nil

	for head != nil {
		next := head.Next
		head.Next = prev
		prev = head
		head = next
	}

	return prev
}
