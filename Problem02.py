"""
Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


from functools import reduce


def solution(numbers):
	# this is the simplest solution using division
	multiples = reduce(lambda x, y: x*y, numbers)
	for i in range( len(numbers) ):
		numbers[i] = int(multiples / numbers[i])
	return numbers

def solution2(numbers):
	# solution without using division, multiple everything without current index
	originals = numbers[:]
	return [ reduce(lambda x, y: x*y, originals[:i] + originals[i+1:]) for i in range( len(numbers) ) ]

if __name__ == '__main__':
	TESTS = {
		'TEST1': [1, 2, 3, 4, 5],
		'TEST2': [3, 2, 1]
	}
	ANSWER = {
		'TEST1': [120, 60, 40, 30, 24],
		'TEST2': [2, 3, 6]
	}

	for test, numbers in TESTS.items():
		try:
			res = solution(numbers)
			assert res == ANSWER[test]
			print(f'PASS: {numbers}')

		except AssertionError:
			print(f'FAIL: {numbers}... expected {ANSWER[test]}')