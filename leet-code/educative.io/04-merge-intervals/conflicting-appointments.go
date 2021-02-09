// https://www.educative.io/courses/grokking-the-coding-interview/qVV79nGVgAG

/*
 * Given an array of intervals representing ‘N’ appointments,
 * find out if a person can attend all the appointments.
 *
 * Appointments: [[1,4], [2,5], [7,9]]
 * Output: false
 * Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
 *
 * Appointments: [[6,7], [2,4], [8,12]]
 * Output: true
 * Explanation: None of the appointments overlap, therefore a person can attend all of them.
 */

package main

import (
	"fmt"
	"os"
	"sort"
)

// return `false` if conflicting; else `true`
func conflictingAppointments(intervals [][]int) bool {
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
		current := intervals[i]
		i++

		if i < len(intervals) && current[1] >= intervals[i][0] {
			return false
		}
	}

	return true
}

func main() {
	intervals := [][]int{{1, 4}, {2, 5}, {7, 9}}
	result := conflictingAppointments(intervals)
	if result != false {
		fmt.Println("Wrong answer.")
		os.Exit(1)
	}

	intervals = [][]int{{6, 7}, {2, 4}, {8, 12}}
	result = conflictingAppointments(intervals)
	if result != true {
		fmt.Println("Wrong answer.")
		os.Exit(1)
	}

	intervals = [][]int{{4, 5}, {2, 3}, {3, 6}}
	result = conflictingAppointments(intervals)
	if result != false {
		fmt.Println("Wrong answer.")
		os.Exit(1)
	}
}
