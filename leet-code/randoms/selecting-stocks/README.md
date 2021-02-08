[original question](https://leetcode.com/discuss/interview-question/985132/IBM-or-OA-or-Selecting-Stocks/798958)

Since IBM intern interviews are over, I was thinking of posting this questions because I was not able to answer in the alotted time.

An investor has saved some money and wants to invest in the stock market. There are a number of stocks to choose from, and they want to buy at most 1 share in any company. The total invested cannot exceed the funds available. A friend who is a stock market expert has predicted the value of each stock after 1 year. Determine the maximum profit that can be earned at the end of the year assuming the predictions come true.

**Example**
saving = 250
currentValue = [175, 133, 109, 201, 97]
futureValue = [200, 125, 128, 228, 133]

To maximize profits, the investor should buy stocks at indices 2 and 4 for an investment of 109 + 97 = 206. At the end of the year the stocks are sold for 128+133 = 261, so total profit is 261-206 = 55

**Example**
saving = 30
currentValue = [1,2,4,6]
futureValue = [5,3,5,6]

Output = 6

**Example**
*saving = 500
currentValue = [150, 199, 200, 168, 153]
futureValue = [140, 175, 199, 121, 111]

Output = 0 since all of the stocks lost money*