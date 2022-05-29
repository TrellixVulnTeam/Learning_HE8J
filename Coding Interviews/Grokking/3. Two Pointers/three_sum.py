def triple_sum_to_zero(arr) :
    arr.sort()
    ans = []
    for i in range(len(arr)):
        #if same as previous one just skip
        if (i > 0 and  arr[i] == arr[i-1]):
            continue
        first_num = arr[i]
        pairs = search_pair(arr, i + 1, -first_num)
        ans += [[first_num] + pair for pair in pairs]
    return ans


def search_pair(arr, starting_index, target):
    left = starting_index
    right = len(arr) - 1
    pairs = []
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target :
            pairs.append([arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr [right + 1]:
                right -= 1
        elif target > sum:
            left += 1
        else :
            right -= 1
    return pairs

arr = [-3, 0, 1, 2, -1, 1,-2]
print(triple_sum_to_zero(arr))