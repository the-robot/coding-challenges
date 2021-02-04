// https://leetcode.com/problems/backspace-string-compare/

package main

func backspaceCompare(S string, T string) bool {
	index1 := len(S) - 1
	index2 := len(T) - 1

	for index1 >= 0 || index2 >= 0 {
		i1 := getNextValidCharacter(S, index1)
		i2 := getNextValidCharacter(T, index2)

		if i1 < 0 && i2 < 0 {
			return true
		}
		if i1 < 0 || i2 < 0 {
			return false
		}
		if S[i1] != T[i2] {
			return false
		}

		index1 = i1 - 1
		index2 = i2 - 1
	}

	return true
}

func getNextValidCharacter(str string, index int) int {
	backspaceCount := 0

	for index >= 0 {
		if string(str[index]) == "#" { // found a backspace
			backspaceCount++
		} else if backspaceCount > 0 { // a non backspace character
			backspaceCount--
		} else {
			break
		}

		index -= 1 // skip a backspace or a valid character
	}

	return index
}
