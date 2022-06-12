from heapq import *

class Interval:
    def __init__(self, start, end, load):
        self.start = start
        self.end = end

    
    def print_interval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]", end='')

class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex 

    def __lt__(self, other):
        return self.interval.start < other.interval.start

def find_employee_free_time(schedule):
    if schedule is None:
        return []
    
    # n is number of employees
    n = len(schedule)
    result, minHeap = [], []

    #inset the first interval of each employee
    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))  
    
    previousInterval = minHeap[0].interval
    while minHeap:
        queueTop = heappop(minHeap)
        
        #if not overlapping
        if previousInterval.end < queueTop.interval.start:
            result.append(Interval(previousInterval.end, queueTop.interval.start))
            previousInterval = queueTop.interval

        else:
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval
            
            employeeSchedule = schedule[queueTop.employeeIndex]
            if len(employeeSchedule) > queueTop.intervalIndex + 1: 
                heappush(minHeap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex, queueTop.intervalIndex + 1 ))

        return result