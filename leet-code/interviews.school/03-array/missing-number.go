// https://leetcode.com/problems/missing-number/

package main

func missingNumber(nums []int) int {
	/*
		find the sum if none is missing
		should be: length + sum of indices

		i.e. if input is [3, 0, 1], if none is missing it should be [3, 0, 1, 2]
		sum if none is missing would be 6.
	*/
	sumIfNoneMissing := len(nums)

	// sum from current array
	sums := 0

	for index, num := range nums {
		sumIfNoneMissing += index
		sums += num
	}

	return sumIfNoneMissing - sums
}
