// https://leetcode.com/problems/linked-list-cycle/

package main

// ListNode is a linked list array element
type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	slow := head
	fast := head

	for fast != nil && fast.Next != nil && fast.Next.Next != nil {
		fast = fast.Next.Next // hare (run 2 times faster than tortoise)
		slow = slow.Next      // tortoise (run 1 time at a time)

		if slow == fast {
			// you can call calculateCycleLength method to find cycle length.
			return true
		}
	}

	return false
}

/*
Method to find length of the cycle.
*/
func calculateCycleLength(slow *ListNode) int {
	current := slow.Next
	length := 1

	for current != slow {
		current = current.Next
		length++
	}

	return length
}
