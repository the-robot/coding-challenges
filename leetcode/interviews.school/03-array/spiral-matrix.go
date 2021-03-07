// https://leetcode.com/problems/spiral-matrix/

package main

func changeDirection(direction string) string {
	switch direction {
	case "right":
		return "down"
	case "down":
		return "left"
	case "left":
		return "up"
	case "up":
		return "right"
	default:
		return "right"
	}
}

func findNextPosition(y, x int, direction string) (int, int) {
	switch direction {
	case "right":
		x++
	case "down":
		y++
	case "left":
		x--
	case "up":
		y--
	}

	return y, x
}

func isOutOfBound(y int, x int, row, col int) bool {
	return y > row-1 || x > col-1 || x < 0 || y < 0
}

func isSeen(seen [][]bool, y, x int) bool {
	return seen[y][x]
}

func nextPosition(position []int, direction string, row, col int) (int, int, string) {
	nextY, nextX := findNextPosition(position[0], position[1], direction)
	// if out of bound, change direction
	if isOutOfBound(nextY, nextX, row, col) {
		direction = changeDirection(direction)
		nextY, nextX := findNextPosition(position[0], position[1], direction)
		return nextY, nextX, direction
	}
	return nextY, nextX, direction
}

func spiralOrder(matrix [][]int) []int {
	row := len(matrix)
	col := len(matrix[0])

	// create a map to track which cell is seen
	// set starting point [0][0] as seen
	visited := make([][]bool, row)
	for i := 0; i < row; i++ {
		visited[i] = make([]bool, col)
	}
	visited[0][0] = true

	// start spiral loop
	position := []int{0, 0} // y, x
	direction := "right"
	blockedCounter := 0 // if 2 means no more place to go

	// to store result
	result := make([]int, row*col)
	result[0] = matrix[0][0]
	index := 1

	for true {
		/*
		   if direction "right", check the one on right
		       - if out of bound; change direction (down) and repeat the loop

		   if direction "down"; check the one below
		       - if out of bound; change direction (left) and repeat the loop

		   if direction "left"; check the one on left
		       - if out of bound; change direction (up) and repeat the loop

		   if direction "up"; check the one on top
		       - if out of bound; change direction (right) and repeat the loop

		   IF not out of bound; and not seen; add the value to result and repeat
		   IF not out of bound; but seen already; add blocked counter to 1
		       - if blocked again (blocked counter = 2) means no more to go
		       - so just stop
		*/
		y, x, newDirection := nextPosition(position, direction, row, col)

		if isOutOfBound(y, x, row, col) || isSeen(visited, y, x) {
			blockedCounter++

			// if 2 means, it has already visited every cell
			if blockedCounter == 2 {
				break
			}

			// if not just change direction and try treversing again
			direction = changeDirection(direction)
			continue
		}

		// update direction and positions
		visited[y][x] = true
		position[0] = y
		position[1] = x
		direction = newDirection

		// reset blocked counter
		blockedCounter = 0

		// keep track of result
		result[index] = matrix[y][x]
		index++
	}

	return result
}
