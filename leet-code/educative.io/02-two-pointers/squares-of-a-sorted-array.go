// https://leetcode.com/problems/squares-of-a-sorted-array/

package main

func sortedSquares(nums []int) []int {
	var left int = 0
	var right int = len(nums) - 1
	var squared = make([]int, len(nums))
	var sqrPtr = len(nums) - 1 // to store where to put next value

	for sqrPtr >= 0 {
		lSquared := nums[left] * nums[left]
		rSquared := nums[right] * nums[right]

		if lSquared > rSquared {
			squared[sqrPtr] = lSquared
			left++
		} else {
			squared[sqrPtr] = rSquared
			right--
		}

		sqrPtr--
	}

	return squared
}
