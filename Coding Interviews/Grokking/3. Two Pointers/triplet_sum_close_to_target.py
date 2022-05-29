'''
Given an array, we want to output the triplet's sum that has the closest value to the target

'''
import math
def triple_closest(arr, target):
    arr.sort()
    closest_sum = 0
    difference_to_target = math.inf
    for i in range(len(arr)): 
        left = i + 1
        right = len(arr) - 1
       
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == target:
                return sum
            elif sum < target :
                left += 1
            elif sum > target:
                right -= 1
            curr_difference = abs(target - sum)
            if curr_difference < difference_to_target:
                difference_to_target = curr_difference
                closest_sum = sum

    return closest_sum
                
arr= [0,1,2]
print(triple_closest(arr, 3))