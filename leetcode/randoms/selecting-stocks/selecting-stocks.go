// https://leetcode.com/discuss/interview-question/985132/IBM-or-OA-or-Selecting-Stocks/798958

package main

import (
	"fmt"
	"sort"
)

func knapsack(values []int, weights []int, saving int) int {
	sack := make([][]int, len(weights)+1)

	// basically calculate every subset of items up to a given weight (capacity)
	for i := 0; i <= len(weights); i++ {

		// create j dimension []int
		sack[i] = make([]int, saving+1)

		for j := 0; j <= saving; j++ {

			if i == 0 || j == 0 {

				// 1st iteration starts with 0
				sack[i][j] = 0

			} else if weights[i-1] <= j {

				// if we can take the item and we stay below weight
				x := values[i-1] + sack[i-1][j-weights[i-1]]
				y := sack[i-1][j]

				if x > y {
					sack[i][j] = x
				} else {
					sack[i][j] = y
				}

			} else {

				sack[i][j] = sack[i-1][j]

			}
		}

	}

	return sack[len(weights)][saving]
}

func getMaxProfit(saving int, currentValues []int, futureValues []int) int {
	values := make([]int, len(currentValues))

	for i := 0; i < len(currentValues)-1; i++ {
		actualValue := futureValues[i] - currentValues[i]
		if actualValue < 0 {
			actualValue = 0
		}
		values[i] = actualValue
	}

	return knapsack(values, currentValues, saving)
}

func main() {
	saving := 250
	currentValue := []int{175, 133, 109, 201, 97}
	futureValue := []int{200, 125, 128, 228, 133}

	// correctStocksIndices := []int{2, 4}
	chosenStockIndices := getMaxProfit(saving, currentValue, futureValue)

	fmt.Println(chosenStockIndices)

	// if !isCorrect(correctStocksIndices, chosenStockIndices) {
	// 	fmt.Println("Wrong answer.")
	// } else {
	// 	fmt.Println("Correct answer.")
	// }
}

func isCorrect(expected []int, chosen []int) bool {
	// compare length
	if len(expected) != len(chosen) {
		return false
	}

	// sort values
	sort.Ints(expected)
	sort.Ints(chosen)

	// if length is the same, check values inside
	for i := 0; i < len(expected); i++ {
		if expected[i] != chosen[i] {
			return false
		}
	}

	return true
}
