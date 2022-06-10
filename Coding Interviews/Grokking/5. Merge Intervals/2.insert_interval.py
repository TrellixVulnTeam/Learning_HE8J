# https://leetcode.com/problems/insert-interval/
from common import *
def insert(intervals, newInterval):
    res = []
    #since it is sorted and non overlaping, we skill everything that end before this new thing starts
    start, end = 0, 1
    for interval in intervals:
        if interval[end] < newInterval[start]:
            res.append(interval)
            continue

        #if we reach here, it means, our new interval overlaps
        if (interval[start] <= newInterval[end]) :
            newInterval[start] = min(interval[start], newInterval[start])
            newInterval[end] = max(interval[end], newInterval[end])
            continue
            
        res.append(newInterval)
        res.append(interval)
    return res
    

    

