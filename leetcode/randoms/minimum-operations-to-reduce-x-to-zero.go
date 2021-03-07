// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

package main

import "math"

func minOperations(nums []int, x int) int {
	totalSum := 0
	for _, num := range nums {
		totalSum += num
	}
	target := totalSum - x

	// not enough numbers to reduce to 0
	if target < 0 {
		return -1
	}

	// target is 0 means we need all numbers to reduce x to 0
	if target == 0 {
		return len(nums)
	}

	left := 0
	right := 0
	windowSum := 0
	maxLength := math.MinInt32

	for ; right < len(nums); right++ {
		windowSum += nums[right]

		for windowSum > target {
			windowSum -= nums[left]
			left++
		}

		if windowSum == target && (right-left+1) > maxLength {
			maxLength = right - left + 1
		}
	}

	if maxLength == math.MinInt32 {
		return -1
	}
	return len(nums) - maxLength
}
