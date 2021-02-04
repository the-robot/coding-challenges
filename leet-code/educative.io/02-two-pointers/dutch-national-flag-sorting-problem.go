// https://coderbyte.com/algorithm/dutch-national-flag-sorting-problem

package main

import "fmt"

func dutchFlag(nums []int) []int {
	mid := 0
	left := 0
	right := len(nums) - 1

	for mid <= right {
		if nums[mid] == 0 {
			nums[mid], nums[left] = nums[left], nums[mid]
			mid++
			left++
		} else if nums[mid] == 2 {
			nums[mid], nums[right] = nums[right], nums[mid]
			right--
		} else {
			mid++
		}
	}

	return nums
}

func main() {
	var answer = []int{0, 0, 1, 1, 2, 2}
	var nums = []int{2, 0, 0, 1, 2, 1}

	nums = dutchFlag(nums)

	if isCorrect(answer, nums) {
		fmt.Println("Correct Answer")
	} else {
		fmt.Println("Wrong Answer")
	}
}

func isCorrect(answer []int, result []int) bool {
	if len(answer) != len(result) {
		return false
	}

	for i := 0; i < len(answer); i++ {
		if answer[i] != result[i] {
			return false
		}
	}

	return true
}
