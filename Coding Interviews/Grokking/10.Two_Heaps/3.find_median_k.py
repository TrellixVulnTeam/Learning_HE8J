from heapq import heappush, heappop
import heapq
from re import L


class MedianOfAStream:

    def __init__(self):
        self.maxHeap = [] #first half (because usually its minheap, so for max heap we insert the negative)
        self.minHeap = [] # second half

    def find_median_size_k (self, nums, k):
        result = [0.0 for x in range (len(nums) - k + 1)]
        for i in range(0, len(nums)):
            self.insert_num(nums[i])
            self.rebalance_heap()

            # if we at least have k elements, in the window
            if i - k + 1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    result[i-k+1] =  -self.maxHeap[0]/2.0 + self.minHeap[0]/2.0
                else:
                    result[i-k+1] = -self.maxHeap[0]/1.0

            #remove the element going out
            elementToBeRemoved = nums[i-k+1]
            if elementToBeRemoved <= -self.maxHeap[0]:
                self.remove(self.maxHeap, -elementToBeRemoved)
            else:
                self.remove(self.minHeap, elementToBeRemoved)
            
    def insert_num(self, num):
        #if max heap empty or max heap's top is greater, ie num is smaller
        if not self.maxHeap or - self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        
        #either maxheap has 1 greater, or both equal
        #if max heap has 2 greater, push from max heap to min heap


        
    def remove(self, heap, element):
        ind = heap.index(element)

        #copy last to current position and delete last
        heap[ind] = heap[-1]
        del heap[-1]

        # need to rebalance
        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)
        
    def rebalance_heap(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        # if min heap has 1 more, push to max heap to make max heap greater
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))


a = MedianOfAStream()
a.insert_num(3)
a.insert_num(1)
print(f'median is {a.find_median()}')
a.insert_num(4)
print(f'median is {a.find_median()}')
a.insert_num(5)
print(f'median is {a.find_median()}')

# for loop O(N), each num log K to insert/remove O(K) to search for index => N * (K + 2logK) = N*K