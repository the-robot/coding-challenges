// https://leetcode.com/problems/spiral-matrix/

package main

/*
Solution
	- swap row and col (transpose)
	- after that reflect the matrix by column (aka reverse the array)

Example:
[1 2 3]
[4 5 6]
[7 8 9]

0, 0 -> 0, 0 -> 0, 2
0, 1 -> 1, 0 -> 1, 2
0, 2 -> 2, 0 -> 2, 2

1, 0 -> 0, 1 -> 0, 1
1, 1 -> 1, 1 -> 1, 1
1, 2 -> 2, 1 -> 2, 1

2, 0 -> 0, 2 -> 0, 0
2, 1 -> 1, 2 -> 1, 0
2, 2 -> 2, 2 -> 2, 0
*/

func rotate(matrix [][]int) {
	// O(N^2) time complexity with O(1) space complexity
	temp := -1

	// transpose the matrix by reversing the row and column
	for row, numbers := range matrix {
		for col := range numbers {
			if col < row {
				continue
			}

			temp = matrix[row][col]
			matrix[row][col] = matrix[col][row]
			matrix[col][row] = temp
		}
	}

	// reverse the array (each row) inside matrix
	for row, numbers := range matrix {
		for i, j := 0, len(numbers)-1; i < j; i, j = i+1, j-1 {
			temp = matrix[row][i]
			matrix[row][i] = matrix[row][j]
			matrix[row][j] = temp
		}
	}
}
