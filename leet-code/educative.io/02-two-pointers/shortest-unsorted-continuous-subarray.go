// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

package main

import "math"

func findUnsortedSubarray(nums []int) int {
	low := 0
	high := len(nums) - 1

	// find first out of order number from start
	for low < len(nums)-1 && nums[low] <= nums[low+1] {
		low++
	}

	// array is sorted, if low is equal to last index
	if low == len(nums)-1 {
		return 0
	}

	// find first out of order number from last
	for high > 0 && nums[high] >= nums[high-1] {
		high--
	}

	// find the maximum and minimum of the subarray
	subarrayMax := math.MinInt32
	subarrayMin := math.MaxInt32
	for k := low; k <= high; k++ {
		if nums[k] > subarrayMax {
			subarrayMax = nums[k]
		}

		if nums[k] < subarrayMin {
			subarrayMin = nums[k]
		}
	}

	// extend the low
	for low > 0 && nums[low-1] > subarrayMin {
		low--
	}

	// extend the high
	for high < len(nums)-1 && nums[high+1] < subarrayMax {
		high++
	}

	return high - low + 1
}
