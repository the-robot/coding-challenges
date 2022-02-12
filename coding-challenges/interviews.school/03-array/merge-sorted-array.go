// https://leetcode.com/problems/merge-sorted-array/

package main

func merge(nums1 []int, m int, nums2 []int, n int) {
	left := m - 1  // the most right end of number != 0, the number before 0
	right := n - 1 // the most right end of the 0

	for i := m + n - 1; i >= 0; i-- {
		if right < 0 {
			break
		}

		if left >= 0 && nums1[left] > nums2[right] {
			/* if the number behind in num1 is greater than
			   the current number from num2
			   copy the number behind in num1 to current i'th position
			   and check num2 with the one behind */
			nums1[i] = nums1[left]
			left--
		} else {
			/*  if the number behind in num1 is not greater than
			    the current number from num2
			    just simply put the num2 at the current i'th position
			    TLDR; just put in front of the number behind in num1 */
			nums1[i] = nums2[right]
			right--
		}
	}
}
