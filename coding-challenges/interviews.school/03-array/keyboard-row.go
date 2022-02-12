// https://leetcode.com/problems/keyboard-row/

package main

import "strings"

func binarySearch(characters []string, character string) bool {
	/* run time for binary search is O(log(n)) */
	if len(characters) == 1 {
		return characters[0] == character
	}

	// get character ord
	charOrd := []rune(character)[0]

	// get mid valid
	midIndex := len(characters) / 2
	midChar := characters[midIndex]
	midCharOrd := []rune(midChar)[0]

	if midChar == character {
		return true
	} else if midCharOrd > charOrd {
		// find character on the left of array
		return binarySearch(characters[0:midIndex], character)
	}

	// find character on the right of array
	return binarySearch(characters[midIndex:len(characters)], character)
}

func getIntByCharacter(toSearch string) int {
	/*
	   since it is using binary search to find
	   3 * O(log(n)) -> O(log(n))
	*/
	keyboard := [][]string{
		{"e", "i", "o", "p", "q", "r", "t", "u", "w", "y"},
		{"a", "d", "f", "g", "h", "j", "k", "l", "s"},
		{"b", "c", "m", "n", "v", "x", "z"},
	}

	for index, keys := range keyboard {
		if binarySearch(keys, toSearch) {
			return index
		}
	}

	return -1
}

func findWords(words []string) []string {
	result := []string{}

	for _, word := range words {
		// convert everything into lowercase
		toSearch := strings.ToLower(word)

		// store row number and -1 means not valid
		row := -1

		for index, char := range toSearch {
			number := getIntByCharacter(string(char))
			if index == 0 {
				row = number
			} else if row != number {
				row = -1 // set back to not valid
				break
			}
		}

		// if not -1 means it is valid
		if row != -1 {
			result = append(result, word)
		}
	}

	return result
}
