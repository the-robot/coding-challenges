"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""


def solution(numbers, total):
	# sort to ascending order
	numbers = sorted(numbers)

	# find two numbers by two pointers from left and right, and compute combination
	left = 0
	right = len(numbers) - 1

	# O(N)
	while left < right:
		if ( numbers[left] + numbers[right] ) < total:
			left += 1
		elif ( numbers[left] + numbers[right] ) > total:
			right -= 1
		else:
			return [ numbers[left], numbers[right] ]
	return []


if __name__ == '__main__':
	TESTS = {
		'TEST1': [10, 15, 3, 7]
	}
	TOTAL = {
		'TEST1': 17
	}
	ANSWERS = {
		'TEST1': [10, 7]
	}

	for test, numbers in TESTS.items():
		try:
			res = solution(numbers, TOTAL[test])
			assert sorted( res ) == sorted( ANSWERS[test] )
			print(f'PASS: {numbers}')

		except AssertionError:
			print(f'FAIL: {numbers}... expected {ANSWERS[test]}')
