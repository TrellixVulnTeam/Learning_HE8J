'''
Given an array with 0 1 and 2, sort the array in place
start with left and right pointers at both end (lo, hi)
iterate through the array, if we find a 0, put to left of lo
find a one put to right of hi
'''
def in_place_sort(arr):
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[low], arr[i] == arr[i], arr[low]
            low += 1
            i+= 1
        elif arr[i] == 1:
            i += 1
        elif arr[i] == 2:
            arr[high], arr[i] == arr[i], arr[high]
            high -= 1
    return arr

