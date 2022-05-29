'''
Given an array, find triplet smaller than target
'''
def search_pair(arr, target, starting_index):
    left, right = starting_index, len(arr) - 1
    count = 0
    while left < right:
        curr_sum = arr[left] + arr[right]
        #if curr sum is smaller than target, means if left keep the same, right decrease(right - left) times, sum still smaller
        if curr_sum < target:
            count += right - left
            left += 1
        else:
            right -= 1
    return count

def triplet_smaller_than_target_how_many (arr, target):
    count = 0
    arr.sort()
    for i in range (len(arr) - 2):
        target_for_pair = target - arr[i]
        count += search_pair(arr, target_for_pair, i + 1)
    return count

arr = [-1,4,2,1,3]
print(triplet_smaller_than_target_how_many(arr, 5))