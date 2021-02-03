// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

package main

func removeDuplicates(nums []int) int {
	if len(nums) <= 1 {
		return 1
	}

	i := 0
	for _, n := range nums {
		if i < 2 || n > nums[i-2] {
			nums[i] = n
			i++
		}
	}

	return i
}
