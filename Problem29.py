"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent
repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have
no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""

# FYI: I found one person solving with built-in methods like itertools with re
#      https://gist.github.com/joelgrus/a88fd090639e5c6739fbe77f0b3210ec
#      I believe the running time is the same O(N), his code is neat though, solved in few lines (wow)
# Anyhow, I solved the problem without any built-in methods, and using only slicing and dicing


def encode(string):
    index = 0       # keep track of where to add digit (before char)
    output = None

    # O(N)
    for character in string:
        # at the start
        if output is None:
            output = f'{ 1 }{ character }'
    
         # if string[i] match char from output indexer, index+1 means get char associated to current digit
        elif output[index + 1] == character:
            # digit+char before matched character + (increment digit) matched character + digit+char after matched char
            output = f'{ output[:index] }{ int(output[index]) + 1 }{ output[index+1:] }'

        # if char not match, increment index and char, append new to output
        else:
            # +2 becuase index keep track of digits
            index += 2
            output = f'{ output }{ 1 }{ character }'

    return output

def decode(string):
    output = ''

    # iterate by 2, (basically by digits 0...2...4)
    i = 0
    while i < len(string):
        count = int( string[i] )

        # add its character to output
        output += string[i+1]

        # decrement the count and check move to next char or not
        # if count == 0, + 2 (move to another character)
        count -= 1
        if count == 0:
            i += 2
        else:
            string = f'{ string[:i] }{ count }{ string[i+1:] }'

    return output


if __name__ == '__main__':
    ENCODE_TEST = {
        'TEST1': 'AAAABBBCCDAA'
    }
    ENCODE_ANSWERS = {
        'TEST1': '4A3B2C1D2A'
    }

    DECODE_TEST = {
        'TEST1': '4A3B2C1D2A'
    }
    DECODE_ANSWERS = {
        'TEST1': 'AAAABBBCCDAA'
    }

    print('Encoding test running...')
    for test, string in ENCODE_TEST.items():
        try:
            res = encode(string)
            assert res == ENCODE_ANSWERS[test]
            print(f'PASS: {string}')

        except AssertionError:
            print(f'FAIL: {string}... expected {ENCODE_ANSWERS[test]}')

    print()
    print('Decoding test running...')
    for test, string in DECODE_TEST.items():
        try:
            res = decode(string)
            assert res == DECODE_ANSWERS[test]
            print(f'PASS: {string}')

        except AssertionError:
            print(f'FAIL: {string}... expected {DECODE_ANSWERS[test]}')
