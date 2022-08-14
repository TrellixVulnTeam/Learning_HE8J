class Solution:
    def peakIndexInMountainArray(self, arr):
        return self.recursive(0 ,len(arr) - 1, arr)
            
        
    def recursive(self, left, right, arr):
        length = right - left + 1
        middle = length // 2
        middle_guy = arr[left + middle]
        left_of_middle = arr[left + middle -1]
        right_of_middle = arr[left + middle + 1]
        print(f'{left_of_middle} {middle_guy} {right_of_middle}')
        if middle_guy < right_of_middle and middle_guy > left_of_middle:
            return left+middle
        
        if middle_guy > left_of_middle :
            self.recursive(left+middle, right, arr)
        else: 
            self.recursive(left, left+middle-1, arr)
        return 0
        
Solution().peakIndexInMountainArray([1,2,3,4,5,6,5,4,3,2,1]);