// https://leetcode.com/problems/circular-array-loop/

package main

func circularArrayLoop(nums []int) bool {
	N := len(nums)

	for i := 0; i < len(nums); i++ {
		// 0 means it does not move
		if nums[i]%N == 0 {
			continue
		}

		var isForward bool = nums[i] > 0
		var slow int = i
		var fast int = i

		for {
			// slow pointer
			slow = getNext(nums, N, isForward, slow)
			if slow == -1 {
				break
			}

			// fast pointer, moves twice
			fast = getNext(nums, N, isForward, fast)
			if fast == -1 {
				break
			}
			fast = getNext(nums, N, isForward, fast)
			if fast == -1 {
				break
			}

			if slow == fast {
				return true
			}
		}
	}

	return false
}

func getNext(nums []int, N int, isForward bool, currentIndex int) int {
	direction := nums[currentIndex] > 0

	// if moving different direction, its not cyclic loop anymore
	if direction != isForward {
		return -1
	}

	/*
	 * It is moving back itself from itself. I.e.
	 * [5, 2, 3, 2, 1] or [10, 1, 3, 4, 5] and current index is 0
	 * if the nums[currentIndex] % N is 0, means it will comes back to itself.
	 * So return -1 for next index. It is still valid cycle tho.
	 */
	if nums[currentIndex]%N == 0 {
		return -1
	}

	/*
	 * Get next index from current index, works both direction. I.e.
	 * [-2,-17,-1,-2,-2] and current index is 0 means next index is 3
	 * moving from index 0 by -2 right direction is the same as
	 * moving by 3 left direction.
	 */
	return ((currentIndex+nums[currentIndex])%N + N) % N
}
