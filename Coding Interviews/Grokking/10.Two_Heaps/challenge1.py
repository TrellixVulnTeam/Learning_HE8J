from heapq import heappop, heappush


intervals = [[0,1],[2,3], [8,9], [4,6]]

def find_next_intervals(intervals):
    results = [-1 for x in range(len(intervals))]
    maxStartHeap = []
    maxEndHeap = []

    for i in range(len(intervals)):
        heappush(maxStartHeap, (-intervals[i][0], i))
        heappush(maxEndHeap, (-intervals[i][1], i))

    for _ in range (len(intervals)):
        topEnd, topEndIndex = heappop(maxEndHeap)
        print(topEnd, topEndIndex)
        #find nearest
        next_interval = None
        start_index = -1
        while maxStartHeap and - maxStartHeap[0][0] >= - topEnd:
            next_interval, start_index = heappop(maxStartHeap)
        results[topEndIndex] = start_index
    return results

print(find_next_intervals(intervals))