from asyncio import start_server
from heapq import *

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    #used for priority queue
    def __lt__ (self, other) :
        return self.end < other.end

def min_meeting_rooms(meetings):
    #sort it based on start time
    meetings.sort(key=lambda x: x.start)

    minRooms = 0
    minHeap =[]

    for meeting in meetings:
        #remove all meetings that have ended
        while(len(minHeap) > 0 and meeting.start >= minHeap[0].end):
            heappop(minHeap)

        # add the current meeting into the min_heap
        heappush(minHeap, meeting)
        minRooms = max(minRooms, len(minHeap))

    return minRooms

#basically we insert all the meetings into a heap, and remove the meetings that have ended before the new start time, and keep track of the heap size