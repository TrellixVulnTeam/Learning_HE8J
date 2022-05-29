import math
def smallest_subarray_with_given_sum(k, arr):
    windowSize = math.inf
    windowSum = 0

    windowsStart = 0
    for windowEnd in range (len(arr)):
        windowSum += arr[windowEnd]
        #while the sum is equal or greater than k, first time trigger, then shrink the window
        while windowSum >= k :
            #update window size 
            windowSize = min (windowSize, windowEnd - windowsStart + 1)
            #shrink the window
            windowSum -= arr[windowsStart]
            windowsStart += 1
            
    if windowSize == math.inf:
        return 0
    
    return windowSize

print(smallest_subarray_with_given_sum(7,[2,1,5,2,3,2]))
