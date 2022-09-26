Usually used to solve problems in an array.

Usual steps:
1. initialise max_sum, **window_sum** (TBC) and window_start
2. use a for loop, with window_end as the variable
	1. add window_end to the window_sum
	2. if window_end (window_size) is greater than the supposed size, calculate the sum, and then subtract the last element going out and slide the window ahead.

Time complexity will be O(N), as it only loops through the array once.

Sometimes once we reached a condition, we **need to shrink the window**, such that some condition is hit.

May need to use a hashmap to calculate elements in the window.

1. maximum sum of subarray - loop through array, once window size reaches, calculate sum, subtract going out one and move start to the next
2. smallest subarray with given sum - once sum is reached, shrink the window
3. longest substring with distinct k / fruits into basket - extend till window end, put chars in hashmap,  once more than k distinct, shrink, end up with K distinct , keep track of length
4. **no-repeat substring** - keep a hash map to remember last visited position. Iterate through the list, expand the window, until it reaches an already existing char in the hashmap, then we should shrink the window - i.e. move windowStart to the max(last visited position + 1, windowStart) 
5. longest substring with same letters after replacement - expand window, insert char freq into hashmap, and keep count of max_repeat_letter_count. if window size - max_repeat_count is greater than k, we can shrink the window, then max_length would be window size.
6. replacement - same idea as 5
7. pattern exist in string permutation - insert pattern into hashmap, then iterate through the strings - then we reduce freq from hashmap, and increment if it hits zero. we then shrink window size once window size reaches pattern size - i.e increment start
8. find all anagrams - same as 7, but now remember to store the window start
9. smallest window w subarray - same as 7, but now once we matched, we shrink the window as soon as we remove a match -  rmb to keep min length ![[Pasted image 20220824201703.png]]
10. find_word_concatenation 
	1.  Keep the frequency of every word in a **HashMap**.
	2.  Starting from every index in the string, try to match all the words.
	3.  In each iteration, keep track of all the words that we have already seen in another **HashMap**.
	4.  If a word is not found or has a higher frequency than required, we can move on to the next character in the string.
	5.  Store the index if we have found all the words.

All in all
Pseudocode

```
initialise windowStart, some kind of sum 

for windowEnd in range():
		do something here

		hit some kind of condition, shrink window

		maxSum = something 

```

		