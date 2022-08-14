def find_subsets(nums: list):
    nums.sort()
    sets = []
    sets.append([])
    #index of subsets
    startIndex, endIndex = 0,0

    for i in range(len(nums)):
        #if not the first one, and current = previous
        if i > 0 and nums[i] == nums[i-1]:
            #start will be endIndex + 1
            startIndex = endIndex + 1
        endIndex = len(sets) - 1
        for j in range(startIndex, endIndex + 1):
            subset = list(sets[j])
            subset.append(nums[i])
            sets.append(subset)

    return sets

print(find_subsets([1,3,3,5]))