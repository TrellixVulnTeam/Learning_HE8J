def checkInclusion(s1: str, s2: str) -> bool:
    # insert s1 char into hash table
    char_frequency_map = {}
    for character in s1:
        if character in char_frequency_map:
            char_frequency_map[character] += 1
        else:
            char_frequency_map[character] = 1
    
    # print(char_frequency_map)
    windowStart = 0
    windowEnd = 0
    matched = 0
    for windowEnd in range(len(s2)):
        char = s2[windowEnd]
        if char in char_frequency_map:
            char_frequency_map[char] -= 1
            if char_frequency_map[char] == 0:
                matched += 1
        
        if matched == len(char_frequency_map):
            return True

        if windowEnd - windowStart + 1 == len(s1):
            start_char = s2[windowStart]
            if start_char in char_frequency_map:
                if char_frequency_map[start_char] == 0:
                    matched -= 1
                char_frequency_map[start_char] += 1
            windowStart  += 1
    
    # print(char_frequency_map)
    return False

# print(checkInclusion("ab", "eidboaoo"))

def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    low = 0
    high = len(nums) - 1
    i = 0
    while i < high :
        if nums[i] == 0:
            temp = nums[low]
            nums[low] = nums[i]
            nums[i] = temp
            low += 1
            i += 1
        
        elif nums[i] == 1:
            i += 1
            
        elif nums[i]  == 2:
            temp = nums[high]
            nums[high] = nums[i]
            nums[i] = temp
            high -= 1
    
        
        print(nums)
       

arr = [2,0,2,1,1,0]
print(sortColors(arr))