// https://leetcode.com/problems/3sum-closest/

package main

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	closest := math.MaxInt32

	for i := 0; i < len(nums)-2; i++ {
		left := i + 1
		right := len(nums) - 1

		for left < right {
			sum := nums[i] + nums[left] + nums[right]

			// found a triplet with exact sum
			if sum == target {
				return sum
			}

			// save the closest difference
			if abs(target-sum) < abs(target-closest) {
				closest = sum
			}

			if sum > target {
				right-- // need triplet with larget sum, target is smaller
			} else {
				left++ // need triplet with smaller sum, target is larger
			}
		}
	}

	// sum closest sum
	return closest
}

func abs(a int) int {
	if a < 0 {
		return -a
	}

	return a
}
