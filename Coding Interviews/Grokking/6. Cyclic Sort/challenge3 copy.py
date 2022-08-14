def find_smallest_positive_missing(nums, l):
    i = 0
    n = len(nums)
    while i < n:
        correct_index = nums[i] - 1
        if (nums[i] > 0 and nums[i]<= n and nums[i] != nums[correct_index]):
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else: 
            i += 1
    
    missingNumbers = []
    extraNumbers = set()
    for i in range(n):
        if len(missingNumbers)< k:
            if nums[i] != i + 1:
                missingNumbers.append(i+1)
                extraNumbers.add(nums[i])

    i = 1
    while len(missingNumbers) < k:
        candidateNumber = i + n
        if candidateNumber not in extraNumbers:
            missingNumbers.append(candidateNumber)
        i += 1

    return missingNumbers