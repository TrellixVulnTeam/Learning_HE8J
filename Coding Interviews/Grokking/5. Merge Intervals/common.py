class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self):
        return str(self.start) + "," + str(self.end)

    def __lt__(self, object):
        return self.start < object.start



arr = [[5,3],[2,6],[8,10],[15,18]]
intervals = []
for interval in arr:
    intervals.append(Interval(interval[0],interval[1]))
intervals.sort()
for interval in intervals:
    print(interval)