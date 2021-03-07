// https://leetcode.com/problems/toeplitz-matrix/

package main

func isToeplitzMatrix(matrix [][]int) bool {
	row := len(matrix)
	col := len(matrix[0])

	// from bottom-left, loop by row for first bottom-left half
	// except the diagonal from matrix[0][0], it will be checked by col-loop below.
	// therefore j stops when j == 0
	for j := row - 1; j > 0; j-- {
		val := matrix[j][0]

		for i := 1; i < col; i++ {
			// if row is out of matrix; skip
			if j+i > row-1 {
				continue
			}

			diagonalVal := matrix[j+i][i]
			if val != diagonalVal {
				return false
			}
			val = diagonalVal
		}

	}

	// from top-left, loop by col for remaining top-right half
	for i := 0; i < col; i++ {

		val := matrix[0][i]

		for j := 0; j < row; j++ {
			// if col is out of matrix; skip
			if j+i > col-1 {
				continue
			}

			diagonalVal := matrix[j][j+i]
			if val != diagonalVal {
				return false
			}
			val = diagonalVal
		}

	}

	return true
}
