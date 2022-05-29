from re import I


def two_sum (arr, target):

    left, right = 0, len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum < target:
            left += 1
        
        elif sum > target: 
            right += 1
        
        else: 
            return [left, right]
    
    return [-1, -1]
        

def two_sum_hashmethod(arr, target) :
    hash_table = {}
    for i in range (len(arr)):
        if (target - arr[i]) in hash_table:
            return [i, hash_table[target - arr[i]]]
        
        else:
            hash_table[arr[i]] = I

    return [-1, -1]

        
