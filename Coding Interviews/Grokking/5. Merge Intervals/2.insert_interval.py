# https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       
        res = []
        start, end = 0, 1
        for i in range (len(intervals)):
            #new interval end before this interval starts
            if newInterval[end] < intervals[i][start]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # new interval starts after this interval
            elif newInterval[start] > intervals[i][end]:
                res.append(intervals[i])

            else: 
                newInterval = [min(newInterval[start], intervals[i][start]), max(newInterval[end], intervals[i][end])]

        res.append(newInterval)
        return res
        