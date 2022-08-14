def find_all_missing_number(nums):
    i, n = 0, len(nums)
    while i < len(nums):
        print("i is at")
        print(i)
        print("before")
        print(nums)
        correct_index = nums[i] -1
        #if it is at [1,2,3,4,1] and i is at the 4 aka the second one, it will count as pass because correct index is at 0, and the number at correct_index is equal to the curr_num
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
            print("after")
            print(nums)
        else:
            i += 1
            print("skip")
    missingNums = []

    for i in range(n):
        if nums[i] != i + 1:
            missingNums.append(i+1)
    
    return missingNums

# O(n) + O(n-1) + O(n)
print(find_all_missing_number([2,3,1,8,2,3,5,1]))