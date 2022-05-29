# https://leetcode.com/problems/maximum-subarray/

def maximum_subarray_of_size_k(K, arr):

    windowSum, windowStart = 0.0, 0
    max_sum = 0

    for windowEnd in range (len(arr)):
        windowSum += arr[windowEnd]
        
        #windowEnd greater or equal than 4 (0,1,2,3,4) trigger at 4
        if windowEnd >= K - 1:
            max_sum = max(windowSum, max_sum)
            windowSum -= arr[windowStart]
            windowStart += 1
    
    return max_sum


def maximum_subarray(arr):
    temp_accumulator = 0
    max_sum = arr [0] 

    for num in arr:
        temp_accumulator += num
        max_sum = max (max_sum, temp_accumulator)
        if temp_accumulator < 0:
            temp_accumulator = 0
            
    return max_sum
        


def main():
    print(maximum_subarray_of_size_k(2, [1,3,2,6,-1,4,1,8,2]))
    print(maximum_subarray ([1,3,2,6,-1,4,1,8,2]))


if __name__ == "__main__":
    main()