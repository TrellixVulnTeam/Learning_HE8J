
from heapq import *
def topKFrequent(nums, k):
    minHeap = []
    seen = {}
    for num in nums:
        print(num)
        if num not in seen:
            seen[num] = 0
        seen[num] += 1
        print("hlo")
        print((- seen[num], num))
        heappush(minHeap, (- seen[num], num))
    
    result = {}
    while len(result) < k:
        curr = heappop(minHeap)
        print(len(minHeap))
        print(curr)
        if curr[1] not in result:
            result[curr[1]] = 1
    
    return result.keys()

print(topKFrequent([1,1,1,2,2,5], 2))