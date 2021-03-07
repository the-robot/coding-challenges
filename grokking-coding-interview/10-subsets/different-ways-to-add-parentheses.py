# https://leetcode.com/problems/different-ways-to-add-parentheses/

from typing import List

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        result = []
        
        if '+' not in input and '-' not in input and '*' not in input:
            result.append(int(input))
        else:
            for i in range(0, len(input)):
                char = input[i]
                
                if not char.isdigit():
                    # break the equation here and make the recursive calls
                    leftPart = self.diffWaysToCompute(input[0:i])
                    rightPart = self.diffWaysToCompute(input[i+1:])
                    
                    for left in leftPart:
                        for right in rightPart:
                            if char == '+':
                                print(left, right, left + right)
                                result.append(left + right)
                            elif char == '-':
                                print(left, right, left - right)
                                result.append(left - right)
                            else:
                                print(left, right, left * right)
                                result.append(left * right)
        
        return result
