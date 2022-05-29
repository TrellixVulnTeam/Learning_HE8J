# def length_of_longest_substring(str, k) :
#     window_start = 0
#     max_length = 0
#     char_frequency_map = {}
#     max_repeated = 0

#     for window_end in range (len(str)):
#         right_char = str[window_end]

#         if right_char not in char_frequency_map:
#             char_frequency_map[right_char] = 0
#         char_frequency_map[right_char]+= 1

#         max_repeated = max (max_repeated, char_frequency_map[right_char])

#         if (window_end - window_start + 1 - max_repeated) > k :
#             left_char = str[window_start]
#             char_frequency_map[left_char] -= 1
#             window_start += 1
        
#         max_length = max (max_length, window_end - window_start + 1)
#     return max_length

def length_of_longest_substring(arr, k) :
    window_start = 0
    max_length = 0
    max_repeated_ones = 0

    for window_end in range (len(arr)):
        right_char = arr[window_end]

        if arr[window_end] == 1:
            max_repeated_ones += 1

        if (window_end - window_start + 1 - max_repeated_ones) > k :
            if arr[window_start] == 1:
                max_repeated_ones -= 1
            window_start += 1
        
        max_length = max (max_length, window_end - window_start + 1)
    return max_length

print(length_of_longest_substring([1,0,0,1,1,1,1,1,1], 2))