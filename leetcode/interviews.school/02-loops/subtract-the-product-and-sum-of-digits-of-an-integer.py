# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        products = 1
        sums = 0

        while (n > 0):
            # get last digit and remove last digit
            lastDigit = n % 10
            n = int(n / 10)

            products *= lastDigit
            sums += lastDigit

        return products- sums
