from heapq import heappop, heappush



class Job:
    def __init__(self, start, end, load):
        self.start = start
        self.end = end
        self.load =load
    
    def __lt__(self, other):
        return self.end < other.end


def max_cpu_load(jobs):
    minHeap = []
    curr_load = 0
    max_load = 0

    for job in jobs:
    
        #remove ended jobs
        while (len(minHeap) > 0) and job.start >= minHeap[0].end:
            curr_load -= minHeap[0].load
            heappop(minHeap)
        
        heappush(minHeap, job)
        curr_load += job.load
        max_load = max(max_load, curr_load)
    
    return max_load
