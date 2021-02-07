// https://leetcode.com/problems/linked-list-cycle-ii/

package main

// ListNode is a linked list array element
type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	slow := head
	fast := head
	cycleLength := 0

	for fast != nil && fast.Next != nil && fast.Next.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next

		if slow == fast {
			cycleLength = calculateCycleLength(slow)
			break
		}
	}

	// if cycle length is 0; no cycle
	if cycleLength == 0 {
		return nil
	}

	return findStart(head, cycleLength)
}

func calculateCycleLength(slow *ListNode) int {
	current := slow.Next
	length := 1

	for current != slow {
		current = current.Next
		length++
	}

	return length
}

func findStart(head *ListNode, cycleLength int) *ListNode {
	pointer1 := head
	pointer2 := head

	// move pointer2 ahead of cycleLength nodes
	for cycleLength > 0 {
		pointer2 = pointer2.Next
		cycleLength--
	}

	// increment both pointers until they meet at the start of the cycle
	for pointer1 != pointer2 {
		pointer1 = pointer1.Next
		pointer2 = pointer2.Next
	}

	return pointer1
}
