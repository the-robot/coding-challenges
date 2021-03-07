// https://leetcode.com/problems/set-matrix-zeroes/

package main

import "sort"

func inArray(numbers []int, lookup int) bool {
	// edge case
	if len(numbers) == 0 {
		return false
	}

	length := len(numbers)
	center := length / 2
	centerValue := numbers[center]

	if length == 1 {
		if centerValue == lookup {
			return true
		}
		return false
	}

	if centerValue > lookup {
		return inArray(numbers[0:center], lookup)
	} else {
		return inArray(numbers[center:length], lookup)
	}
}

func setZeroes(matrix [][]int) {
	rows := []int{}
	cols := []int{}

	// find where the original zeros are
	for row, numbers := range matrix {
		for col, number := range numbers {
			if number == 0 {
				rows = append(rows, row)
				cols = append(cols, col)
			}
		}
	}

	// sort numbers (so we can do binary search easily)
	sort.Ints(rows)
	sort.Ints(cols)

	// set 0 if row or col is in zeros list
	for row, numbers := range matrix {
		rowIsZero := inArray(rows, row)
		for col := range numbers {
			if rowIsZero || inArray(cols, col) {
				matrix[row][col] = 0
			}
		}
	}
}
