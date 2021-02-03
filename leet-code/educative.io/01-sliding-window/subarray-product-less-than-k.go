// https://leetcode.com/problems/subarray-product-less-than-k/

package main

func numSubarrayProductLessThanK(nums []int, k int) int {
	if k <= 1 {
		return 0
	}

	prod := 1 // to store multiplier
	counter := 0
	left := 0

	for right, num := range nums {
		prod *= num

		for prod >= k {
			prod /= nums[left]
			left += 1
		}

		counter += right - left + 1
	}

	return counter
}
