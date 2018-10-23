"""
Given a string of round, curly and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the strign "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def match(x, y):
    curly = ( '{', '}' )
    square = ( '[', ']' )
    rnd = ( '(', ')' )

    if (x in curly and y in curly) or\
       (x in square and y in square) or\
       (x in rnd and y in rnd):
        return True
    return False

def solution(brackets):
    openings = ['{', '[', '(']
    closings = ['}', ']', ')']

    total_openings = 0
    total_closings = 0
    stack = []

    # 1. FREQUENCY ANALYSIS
    for char in brackets:
        if char in openings:
            total_openings += 1
        else:
            total_closings += 1
    # if opening and closing frequency are not the same
    # not balance
    if total_openings != total_closings:
        return False

    # 2. SEQUENCE ANALYSIS
    for char in brackets:
        # if opening add to stack
        if char in openings:
            stack.append(char)
        # if closing pop from stack and compare
        else:
            try:
                top = stack.pop(-1)
                if not match(top, char):
                    return False
            except (IndexError, ValueError):
                # if not exists
                return False

    # if all passed, balance
    return True


if __name__ == '__main__':
    TESTS = {
        '([])[]({})': True,
        '([)]': False,
        '((()': False,
        ')))(((': False,
        '(){}[])': False,
    }

    for test, result in TESTS.items():
        res = solution(test)

        try:
            assert res == result
            print(f'PASS: {test}')
        except AssertionError:
            print(f'FAIL: {test}... expected {result}, got {res}')
