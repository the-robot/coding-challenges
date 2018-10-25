/*
* Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
* Numbers can be 0 or negative.
* For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6 and 5.
* [5, 1, 1, 5] should return 10, since we pick 5 and 5.
* Follow-up: Can you do this in O(N) times and constant space?
*/

package main

import (
    "fmt"
    "sort"
)


type Test struct {
    Numbers []int
    Answer  int
}


func max(numbers []int) int {
    // to prevent sort on original array
    n := make([]int, len(numbers))
    copy(n, numbers)
    sort.Ints(n)
    return n[len(n)-1]
}

func index(numbers []int, tolook int) int {
    for i:=0; i<len(numbers); i++ {
        if numbers[i] == tolook {
            return i
        }
    }
    return -1
}


func solution(test Test) int {
    numbers := test.Numbers

    // find max
    var max_num int = max(numbers)

    // if len numbers is <= 2, or index of max is center in 3 numbers
    // return max_num (cannot have adjacent)
    if len(numbers) <= 2 || ( len(numbers) == 3 && index(numbers, max_num) == 1 ) {
        return max_num
    }

    return max_num
}

func main() {
    test1 := Test {
        Numbers: []int {2, 4, 6, 2, 5},
        Answer: 13,
    }
    test2 := Test {
        Numbers: []int {5, 1, 1, 5},
        Answer: 10,
    }
    tests := []Test {test1, test2}

    for i:=0; i<len(tests); i++ {
        solution( tests[i] )
    }
}
