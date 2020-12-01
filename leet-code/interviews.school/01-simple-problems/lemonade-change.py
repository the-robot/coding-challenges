# https://leetcode.com/problems/lemonade-change/

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            
            elif bill == 10:
                # you must have minimum 1 $5 change
                if five == 0:
                    return False
                ten += 1
                five -= 1

            elif bill == 20:
                # give by either 1 $5 and 1 $10 change
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1

                # or 3 $5 change
                elif five >= 3:
                    five -= 3

                else:
                    return False 

        return True
