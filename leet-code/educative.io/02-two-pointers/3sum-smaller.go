// https://www.lintcode.com/problem/3sum-smaller/description

import "sort"

/**
 * @param nums:  an array of n integers
 * @param target: a target
 * @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
 */
func threeSumSmaller(nums []int, target int) int {
	sort.Ints(nums)
	smallers := 0

	for i := 0; i < len(nums)-2; i++ {
		left := i + 1
		right := len(nums) - 1

		for left < right {
			sum := nums[i] + nums[left] + nums[right]

			if sum < target {
				// since nums[right] >= nums[left], we can replaced num[right]
				// with any number between indices left and right to get a sum
				// less than the target sum
				smallers += right - left
				left++
			} else {
				right--
			}
		}
	}

	return smallers
}
