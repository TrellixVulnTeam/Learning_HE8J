def longest_substring_with_not_more_than_k_distinct_char (arr, K) :
    max_length = 0
    window_start = 0
    char_list = {}
    
    for window_end in range(len(arr)):
        letter = arr[window_end]

        #insert character in hashtable
        if letter not in char_list:
            char_list[letter] = 0
        char_list[letter] += 1


        while len(char_list) > K :
            #shrink the window
            left_char = arr[window_start]
            char_list[left_char] -=1
            if (char_list[left_char] == 0) :
                del char_list[left_char]
            window_start += 1
        
        max_length = max (max_length, window_end - window_start + 1)

    return max_length
print(longest_substring_with_not_more_than_k_distinct_char("0122", 2))
print(longest_substring_with_not_more_than_k_distinct_char("araaci", 1))
print(longest_substring_with_not_more_than_k_distinct_char("cbbebi", 3))



        

