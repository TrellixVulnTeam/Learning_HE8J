def find_smallest_positive_missing(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct_index = nums[i] - 1
        if (nums[i] > 0 and nums[i]<= n and nums[i] != nums[correct_index]):
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else: 
            i += 1
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1