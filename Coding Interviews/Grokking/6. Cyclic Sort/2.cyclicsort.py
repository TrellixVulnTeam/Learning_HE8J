def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[correct_index] != nums[i]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
        
        return nums

# time complexity is O(n) + O(n-1)
# O(n) like normal while loop, o(n-1)is the xtra total amount of swapping (max)