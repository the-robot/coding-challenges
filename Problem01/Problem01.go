/*
* Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
* For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
* Bonus: Can you do this in one pass?
*/

package main

import (
    "fmt"
    "os"
    "sort"
)


type Test struct {
    Numbers []int
    Total   int
    Answer  bool
}


func solution(test Test) bool {
    numbers := test.Numbers
    total := test.Total

    // sort numbers in ascending order
    sort.Ints(numbers)

    // indices for left and right
    var left int = 0
    var right int = len(numbers) - 1

    // O(N)
    // find two numbers by two indices from left and right, and compute combinations
    for left < right {
        if ( numbers[left] + numbers[right] ) < total { 
            left++
        } else if ( numbers[left] + numbers[right] ) > total {
            right--
        } else {
            return true
        }
    }

    return false
}


func main() {
    // Tests
    test1 := Test {
        Numbers: []int {10, 15, 3, 7},
        Total: 17,
        Answer: true,
    }
    tests := []Test {test1}

    for i:=0; i<len(tests); i++ {
        if tests[i].Answer != solution(tests[i]) {
            fmt.Fprintf(os.Stderr, "FAIL: %v... expected %t\n",
                        tests[i].Numbers, tests[i].Answer)
            continue
        }

        fmt.Printf("PASS: %v\n", tests[i].Numbers)
    }
}
