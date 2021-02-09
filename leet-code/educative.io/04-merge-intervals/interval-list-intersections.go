// https://leetcode.com/problems/interval-list-intersections/

package main

func intervalIntersection(firstList [][]int, secondList [][]int) [][]int {
	if len(firstList) == 0 || len(secondList) == 0 {
		return [][]int{}
	}

	var result [][]int

	i := 0
	j := 0

	for i < len(firstList) && j < len(secondList) {
		a := firstList[i]
		b := secondList[j]

		// check if the interval firstList[i] intersects with secondList[j]
		// check if one of the interval's start time lies within the other intervals
		if (a[0] >= b[0] && a[0] <= b[1]) || (b[0] >= a[0] && b[0] <= a[1]) {
			start := a[0]
			if b[0] > a[0] {
				start = b[0]
			}

			end := a[1]
			if b[1] < a[1] {
				end = b[1]
			}

			result = append(result, []int{start, end})
		}

		// move next from the interval which finishes first
		if a[1] < b[1] {
			i++
		} else {
			j++
		}
	}

	return result
}
