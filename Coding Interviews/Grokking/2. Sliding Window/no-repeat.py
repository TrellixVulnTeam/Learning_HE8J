# def longest_substring_no_repeat(arr):
#     char_list = {}
#     window_start = 0
#     max_length = 0

#     for window_end in range (len(arr)):
#         right_char = arr[window_end]

#         #IF THE CHAR IS IN, we delete the previous one until char not in
#         while right_char in char_list:
#             left_char = arr[window_start]
#             del char_list[left_char]
#             window_start += 1

#         #add into hashtable, if not in
#         if right_char not in char_list:
#             char_list[right_char] = 1
        
#         max_length = max(max_length, window_end - window_start + 1)
#     return max_length

#better version
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
def longest_substring_no_repeat(arr):
    char_list = {}
    window_start = 0
    max_length = 0

    for window_end in range (len(arr)):
        right_char = arr[window_end]

        #IF THE CHAR IS IN
        if right_char in char_list:
            #if window start already ahead, just keep ahead, if not u move it 1 forward to the right char
            window_start = max (window_start, char_list[right_char] + 1)

        #insert
        char_list[right_char] = window_end
    
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(longest_substring_no_repeat("aabccbb"))
print(longest_substring_no_repeat("abbbb"))
print(longest_substring_no_repeat("abccde"))

        