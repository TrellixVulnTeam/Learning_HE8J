def find_corrupted(nums) :
    i = 0
    while i < len(nums):
        correct_position = nums[i] - 1
        if (nums[i] != nums[correct_position]):
            nums[i], nums[correct_position] = nums[correct_position], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]

    return [-1, -1]    