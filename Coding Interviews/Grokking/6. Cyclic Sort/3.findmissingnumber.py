def find_missing_number(nums):
    i, n = 0, len(nums)
    while i < len(nums):
        correct_index = nums[i]
        if nums[i] < n and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
        print(nums)
    
    for i in range(n):
        if nums[i] != i:
            return i
    
    return n

# O(n) + O(n-1) + O(n)
find_missing_number([4,0,3,1])