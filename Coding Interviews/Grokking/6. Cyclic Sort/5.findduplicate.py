def find_duplicate(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            correct_index = nums[i] -1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                return nums[i]
        else:
            i += 1
        
    return -1
    
    

# O(n) + O(n-1) + O(n)
print(find_duplicate([1,4,4,3,2]))