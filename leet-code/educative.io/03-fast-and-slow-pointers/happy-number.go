// https://leetcode.com/problems/happy-number/

package main

/*
 * Happy number is equal to 1. It means the number is happy number if there's no cycle.
 * Square sum of 1 is also 1 (no cycle).
 *
 * So if it is not a happy number (has cycle), fast pointer will keep repeating. I.e.
 *
 * Slow Fast (19, happy number)
 *   82   68
 *   68    1
 *  100    1
 *    1    1
 *
 * Slow Fast (24, not happy number)
 *   20    4
 *    4   37
 *   16   89
 *   37   42
 *   58    4
 *   89   37
 *  145   89
 *   42   42
 */
func isHappy(n int) bool {
	slow := findSquareSum(n)
	fast := findSquareSum(findSquareSum(n))

	for slow != fast {
		slow = findSquareSum(slow)
		fast = findSquareSum(findSquareSum(fast))
	}

	return slow == 1
}

func findSquareSum(num int) int {
	sum := 0
	digit := 0

	for num > 0 {
		digit = num % 10
		sum += digit * digit
		num /= 10
	}

	return sum
}
