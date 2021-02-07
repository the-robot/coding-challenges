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

	headFirstHalf := head           /* 1 -> 2 -> 3 -> 4 */
	headSecondHalf := reverse(slow) /* reverse the mid-end, 4 -> 3 */

	/*
		First iteration
			head -> {
				1 -> 2
				2 -> 3
				3 -> 4
				4 -> nil
			}
			reversed half -> {
				4 -> 3
				3 -> nil
			}

			headFirstHalf = 1
			headSecondHalf = 4

			temp = 2
			headFirstHalf.Next = 4
			headFirstHalf = 2

			... 1 -> 4 -> 3 -> nil

			temp = 3
			headSecondHalf.Next = 2
			headSecondHalf = 3

			... 1 -> 4 -> 2 -> 3

		Second iteration
			head -> {
				1 -> 4
				4 -> 2
				2 -> 3
				3 -> nil
			}
			reversed half -> {
				4 -> 3
				3 -> nil
			}

			headFirstHalf = 2
			headSecondHalf = 3

			temp = nil
			headFirstHalf.Next = 3
			headFirstHalf = 3

			... 1 -> 4 -> 2 -> 4 -> nil

			temp = nil
			headSecondHalf.Next = 3 (now 3 is pointing itself, headSecondHalf is already 3)
			headSecondHalf = nil

			... 1 -> 4 -> 2 -> 3 -> 3 ...... (3 is pointing itself)

		> since headSecondHalf = nil, iteration stops

		after iteration, headFirstHalf = 3
		since it is not equal to nil, set it's next to nil
		means we removed the pointer 3, pointing itself

		so answer is 1 -> 4 -> 2 -> 3
	*/
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
