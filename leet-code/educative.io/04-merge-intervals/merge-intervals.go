// https://leetcode.com/problems/merge-intervals/

package main

import "sort"

func merge(intervals [][]int) [][]int {
	var result [][]int

	// sort array
	sort.Slice(intervals[:], func(i, j int) bool {
		for a := range intervals[i] {
			if intervals[i][a] == intervals[j][a] {
				continue
			}
			return intervals[i][a] < intervals[j][a]
		}
		return false
	})

	for i := 0; i < len(intervals); {
		merged := intervals[i]
		i++

		for i < len(intervals) && merged[1] >= intervals[i][0] {
			if intervals[i][1] > merged[1] {
				merged[1] = intervals[i][1]
			}
			i++
		}

		result = append(result, merged)
	}

	return result
}
