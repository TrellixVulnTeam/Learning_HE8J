def find_all_duplicates(nums):
    i, n = 0, len(nums)
    while i < len(nums):
        correct_index = nums[i] -1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

        else:
            i += 1
            print("skip")
    duplicateNums = []

    for i in range(n):
        if nums[i] != i + 1:
            duplicateNums.append(i+1)
    
    return duplicateNums

# O(n) + O(n-1) + O(n)
print(find_all_duplicates([2,3,1,8,2,3,5,1]))