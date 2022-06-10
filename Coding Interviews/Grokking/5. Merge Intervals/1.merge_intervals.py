def merge(interval_list):
    interval_list.sort(key= lambda x: x[0])
    start = interval_list[0][0]
    end = interval_list[0][1]
    merged = []
    for i in range(1, len(interval_list)):
        curr_interval = interval_list[i]
        curr_interval_start = curr_interval[0]
        curr_interval_end = curr_interval[1]
        
        #if they overlap, we expand the interval to make the end larger
        if end >= curr_interval_start:
            end = max (end, curr_interval_end)
        #if they dont, we add the prev interval in, and set the start and end to the current one
        else:
            merged.append([start, end])
            start = curr_interval_start
            end = curr_interval_end
    
    #add the last one in
    merged.append([start, end])
    return merged


arr = [[1,3],[2,6],[8,10],[15,18]]
print(merge(arr))