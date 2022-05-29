#essentially same as longest_substring with no more than K with K = 2
#https://leetcode.com/problems/fruit-into-baskets/submissions/
def totalFruit(self, fruits):
    maxLength = 0
    windowStart = 0
    char_frequency = {}
    
    for windowEnd in range(len(fruits)):
        
        letter = fruits[windowEnd]
        
        if letter not in char_frequency:
            char_frequency[letter] = 0
        char_frequency[letter] += 1
        
        while len(char_frequency) > 2:
            left_char = fruits[windowStart]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            windowStart += 1
        
        maxLength = max (maxLength, windowEnd - windowStart + 1)
    return maxLength
    
