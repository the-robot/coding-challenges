"""
Write an algorithm to justify text. Given a sequence of words and an integer line
length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
there should be at least one space between each word. Pad extra spaces when
necessary so that each line has exactly length k.

Spaces should be distributed as equally as possible, with the extra spaces,
if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side
with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps",
"over", "the", "lazy", "dog"] and k = 16, you should return the following:


"the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

def divide(words, length):
	# store the length of total words that can be in current line
	s_words = {}
	# keep track how many lines are there
	line = 1
	line_length = 0

	# divide words in line based on the length
	for word in words:
		# new line, then just add the word and increment
		if line_length == 0:
			s_words[ str(line) ] = [word]
			line_length += len(word)

		# total line length + next word + 1 (space between) <= length, then add
		elif line_length + len(word) + 1 <= length:
			s_words[ str(line) ].append(word)
			# increment current line total length + 1 (space between)
			line_length += len(word) + 1

		# if cannot fix in one line
		else:
			# go to next line and reset line length to 0 then add len(next word)
			line += 1
			s_words[ str(line) ] = [word]
			line_length = len(word)

	return s_words

def solution(words, length):
	# figure out how many words in fit in the length
	# find remaining length (length - total words)
	# distribute the remaining length equally between words as spaces

	divided_words = divide(words, length)
	formatted = {}

	for line_number, words in divided_words.items():
		# create empty string on start
		formatted[ line_number ] = ''
		# find diff (spaces left to add between words)
		diff = length - len(' '.join(words))
		# just create sentence (with one space in between)
		formatted[ line_number ] = ' '.join(words)
		i = 0

		# for diff (spaces left to be added)
		if diff > 0:
			# iterate through words
			while i < len(words):
				if diff != 0:
					# if last word, go back the the start of the sentence
					if i == len(words) - 1:
						i = 0

					# find where to add the index
					whereto = formatted[line_number].find(words[i]) + len(words[i])
					sentence = formatted[line_number]
					formatted[line_number] = sentence[:whereto] + ' ' + sentence[whereto:]

					# decrement diff (spaces left to be added) and increment words indexer
					diff -= 1
					i += 1

				# if no more spaces left to add, just break
				else:
					break

	# join sentences with new line and return
	return '\n'.join( formatted.values() )


if __name__ == '__main__':
	WORDS = {
		'TEST1': ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
	}
	LENGTH = {
		'TEST1': 16
	}
	SOLUTION = {
		'TEST1': """the  quick brown\nfox  jumps  over\nthe   lazy   dog"""
	}

	
	for test, words in WORDS.items():
		try:
			res = solution(words, LENGTH[test])
			assert res == SOLUTION[test]
			print(f'PASS: {test}')

		except AssertionError:
			print(f'{"FAIL":9}: {test}')
			print(f'{"WORDS":9}: {words}')
			print(f'{"K":9}: {LENGTH[test]}')
			print(f'EXPECTED :\n{SOLUTION[test]}', end='\n\n')