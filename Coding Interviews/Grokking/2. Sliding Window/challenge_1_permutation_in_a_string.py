'''
for this question, we are trying to find whether the string contains any permutation of the pattern
'''


def find_permutation(str, pattern):
    #insert the pattern into a hashtable 
    #iterate through the string, for  each char, we minus off the count
    #then after the substring of length of pattern, we see how many matches there is
    # if the matches is the sameas the length of the pattern, we return true
    #if not, we move on, move window end and window start one to the right
    char_frequency = {}
    for letter in pattern:
        if letter not in char_frequency:
            char_frequency[letter] = 0
        char_frequency[letter] += 1

    window_start = 0
    matched = 0
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True
        
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
        
    return False

print(find_permutation("oidbcaf", "abc"))
