from turtle import back


#here index is our starting index, since we starting from behind, index is from behind
def get_next_valid_char_index(str, index):
    backspace_count = 0
    while index >= 0:
        if str[index] =='#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break  #if not a backspace, and no more backspaces
        index -= 1

    return index

def compare_strings(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) -1

    while index1 >= 0 or index2>=0:
        i1 = get_next_valid_char_index(str1, index1)
        i2 = get_next_valid_char_index(str2, index2)
        if i1 < 0 and i2 < 0: #both reach end, and everything b4 matches
            return True
        if i1 < 0 or i2 <0: #one reaches end
            return False
        if str1[i1] != str2[i2]: #doesn't match
            return False
        index1 = i1 - 1
        index2 = i2 - 1
    
    return True 

test = "xyz##"
test2 = "xyz#abc####"
print(compare_strings(test, test2))