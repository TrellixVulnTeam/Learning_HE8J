def search_pair(arr, starting_index, target):
    left, right = starting_index, len(arr) - 1
    pairs = []
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            pairs.append([arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr [left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1

    return pairs

def quad_sum(arr, target):
    arr.sort()
    quad = []
    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i + 1,len(arr)-2):
            if j > i + 1 and arr[j] == arr[j-1]:
                continue
            desired_pair_target = target - arr[i] - arr[j]
            pairs = search_pair(arr, j+1, desired_pair_target)
            quad += [[arr[i], arr[j]] + pair for pair in pairs]
    return quad
arr = [4,1,2,-1,1,-3]
print(quad_sum(arr, 1 ))