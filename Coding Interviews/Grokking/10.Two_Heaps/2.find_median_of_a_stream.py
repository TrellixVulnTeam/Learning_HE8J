from heapq import heappush, heappop
from re import L


class MedianOfAStream:
    maxHeap = [] #first half (because usually its minheap, so for max heap we insert the negative)
    minHeap = [] # second half

    def insert_num(self, num):
        #if max heap empty or max heap's top is greater, ie num is smaller
        if not self.maxHeap or - self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        
        #either maxheap has 1 greater, or both equal
        #if max heap has 2 greater, push from max heap to min heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        # if min heap has 1 more, push to max heap to make max heap greater
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
    
    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0]/2.0 + self.minHeap[0]/2.0
        
        return -self.maxHeap[0]/1.0


a = MedianOfAStream()
a.insert_num(3)
a.insert_num(1)
print(f'median is {a.find_median()}')
a.insert_num(4)
print(f'median is {a.find_median()}')
a.insert_num(5)
print(f'median is {a.find_median()}')

