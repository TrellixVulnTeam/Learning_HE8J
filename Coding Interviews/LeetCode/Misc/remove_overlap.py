import math
def eraseOverlapIntervals(intervals) -> int:
    earliestEnd = sorted(intervals, key=lambda x: x[1])
    
    previousEnd = -math.inf
    remove = 0
    for start, end in earliestEnd:
        if start < previousEnd:
            remove += 1
        else:
            previousEnd = end
    
    return remove