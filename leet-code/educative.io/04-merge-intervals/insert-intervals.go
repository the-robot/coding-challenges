// https://leetcode.com/problems/insert-interval/

package main

import (
	"sort"
)

func insert(intervals [][]int, newInterval []int) [][]int {
	// O(N)
	var result [][]int

	// skip and add to result
	i := 0
	for ; i < len(intervals) && intervals[i][1] < newInterval[0]; i++ {
		result = append(result, intervals[i])
	}

	// merge all intervals that overlap with the newInterval
	for ; i < len(intervals) && intervals[i][0] <= newInterval[1]; i++ {
		if intervals[i][0] < newInterval[0] {
			newInterval[0] = intervals[i][0]
		}

		if intervals[i][1] > newInterval[1] {
			newInterval[1] = intervals[i][1]
		}
	}

	// insert the new interval
	result = append(result, newInterval)

	// add the remaining
	for ; i < len(intervals); i++ {
		result = append(result, intervals[i])
	}

	return result
}

func solutionWithMergeInterval(intervals [][]int, newInterval []int) [][]int {
	// O(N * logN)
	var result [][]int

	intervals = append(intervals, newInterval)

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
