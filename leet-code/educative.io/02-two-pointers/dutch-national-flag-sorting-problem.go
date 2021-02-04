// https://coderbyte.com/algorithm/dutch-national-flag-sorting-problem

package main

import "fmt"

func dutchFlag(nums []int) []int {
	i := 0
	left := 0
	right := len(nums) - 1

	for i <= right {
		if nums[i] == 0 {
			nums[i], nums[left] = nums[left], nums[i]
			i++
			left++
		} else if nums[i] == 2 {
			nums[i], nums[right] = nums[right], nums[i]
			right--
		} else {
			i++
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
