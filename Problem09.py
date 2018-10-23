"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6 and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) times and constant space?
"""


def largest(numbers):
    return max(numbers)

def solution(numbers):
    max_num = largest(numbers)

    # if total numbers is <= 2, return (cannot have adjacent)
    if len(numbers) <= 2 or ( len(numbers) == 3 and numbers.index(max_num) == 1 ):
        return max_num

    # if total numbers == 3, and index of largest != 1 (then add first or last index)
    elif len(numbers) == 3 and numbers.index(max_num) != 1:
        index = numbers.index(max_num)
        return numbers[0] + numbers[2]

    # else, do divide and conquer
    else:
        index = numbers.index(max_num)
        left = 0
        right = 0

        # if not index is first one or the one after the first
        if index > 1:
            left += solution( numbers[:index-1] )

        # if not index is last one or the one before the last
        if index < ( len(numbers)-2 ):
            right += solution( numbers[index+2:] )

        return max_num + left + right


if __name__ == '__main__':
    # test cases
    TESTS = {
        'TEST1': [2, 4, 6, 2, 5],
        'TEST2': [5, 1, 1, 5],
    }
    # solutions
    RESULTS = {
        'TEST1': 13,
        'TEST2': 10,
    }

    
    for test, values in TESTS.items():
        res = solution(values)

        try:
            assert res == RESULTS[test]
            print(f'PASS: {values}')
        except AssertionError:
            print(f'FAIL: {values}... excepted {RESULTS[test]}, got {res}')
