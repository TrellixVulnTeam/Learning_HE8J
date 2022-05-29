#given a pattern, find the smallest substring in the string that contains all the char in patterns
'''
1. insert alll the pattern's character in a hash map
2. interate through the string, if the char is in the hash map, decrease the count
3. while matched count is same as pattern size, we shrink the window
'''

from cgitb import small
from operator import le
from re import sub


def find_substring(str, pattern):

    char_frequency = {}
    window_start = 0

    for letter in pattern:
        if letter not in char_frequency:
            char_frequency[letter] = 0
        char_frequency[letter] += 1
    
    matched = 0
    substr_start = 0 
    min_length = len(str) + 1

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        #once enough matches, we shrink the window from the start
        while matched == len(char_frequency):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start
            
            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                #if it is zero, means it is essential, so we minus off the matched
                if char_frequency[left_char] == 0:
                    matched -=1
                    #out already so we add back th frequency
                char_frequency[left_char] += 1
        
    if min_length > len(str):
        return ""
    
    return str[substr_start: substr_start+min_length]

        
    
    

print(find_substring("aabdec", "abc"))