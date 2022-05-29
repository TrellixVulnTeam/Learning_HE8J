def length_of_longest_substring(str, k):
    window_start = 0
    frequency_map = {}
    max_length = 0
    max_repeat_letter_count = 0

    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1

        
        max_repeat_letter_count = max (max_repeat_letter_count, frequency_map[right_char])

        #ensure that at any point, when we replace still can
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        max_length = max (max_length, window_end - window_start + 1)


    return max_length 

print(length_of_longest_substring("aabccdebb", 2))
