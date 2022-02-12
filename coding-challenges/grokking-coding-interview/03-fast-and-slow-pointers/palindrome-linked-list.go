// https://leetcode.com/problems/palindrome-linked-list/

package main

// ListNode is a linked list array element
type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}

	// find middle of the Linked List
	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}

	// reverse the mid-end I.e.
	// 1 -> 2 -> 3 -> 3 -> 2 -> 1 will become
	// 1 -> 2 -> 3 -> 1 -> 2 -> 3
	headSecondHalf := reverse(slow)

	// compare start-mid and mid-end
	for headSecondHalf != nil {
		if head.Val != headSecondHalf.Val {
			return false
		}
		head = head.Next
		headSecondHalf = headSecondHalf.Next
	}

	// reaching here means start-mid is equal to mid-end
	// aka it's palindromic
	return true
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
