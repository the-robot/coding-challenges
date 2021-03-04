**How to identify the Subsets pattern:**  
- Whenever you are given a sorted array, linked list, or matrix, and are asked to find a certain element, the best algorithm you can use is the Binary Search.
- This pattern describes an efficient way to handle all problems involving Binary Search.

<br/>

The patterns looks like this for an ascending order set:  
1. First, find the middle of start and end. An easy way to find the middle would be: `middle = (start + end) / 2`. But this has a good chance of producing an integer overflow so it’s recommended that you represent the middle as: `middle = start + (end — start) / 2`
2. If the key is equal to the number at index middle then return middle
3. If `key` isn’t equal to the index middle:
    - Check if `key < arr[middle]`. If it is reduce your search to `end = middle — 1`.
    - Check if `key > arr[middle]`. If it is reduce your search to `end = middle + 1`.

<br/>

Problems featuring the Modified Binary Search pattern:  
- Order-agnostic Binary Search (easy)
- Search in a Sorted Infinite Array (medium)

<br/>

| Date | Name | Difficulty | Solution |
|:----:|:-----|:----------:|:--------:|
