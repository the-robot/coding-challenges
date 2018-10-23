#### Daily Coding Problems

- These are my solutions for daily coding problems, it is not uploaded to be used as `copy-paste` answers for the challenges given by [https://www.dailycodingproblem.com](https://www.dailycodingproblem.com)

- You may look at the answers to learn or give me a feedback if you have better solution (as I am also not very good at solving complex stuffs)

![Meme](https://media3.giphy.com/media/BmmfETghGOPrW/giphy.gif?cid=3640f6095bceb4fd6e6e7a4845af57d5)

----

#### Problem 01
> by `Google`

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

----

#### Problem 02
> by `Uber`

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

---  

#### Problem 09
> by `Airbnb`    

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6 and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) times and constant space?

---

#### Problem 27
> by `Facebook`

Given a string of round, curly and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the strign "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

---

#### Problem 28
> by `Palantir`

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. there should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

```
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
```