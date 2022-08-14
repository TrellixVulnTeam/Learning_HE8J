def subsets(nums):
    subsets = []
    subsets.append([])

    for currentNum in nums:
        #take existing subset and add the current number to it
        length_of_subsets = len(subsets)

        #add curr number to each subset
        for i in range(length_of_subsets):
            new_appended = list(subsets[i])
            new_appended.append(currentNum)
            subsets.append(new_appended)
    
    return subsets


print(subsets([1,2,3]))
