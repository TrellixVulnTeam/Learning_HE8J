def intersection(intervals_a, intervals_b):
    result = []
    i, j, start, end = 0, 0, 0, 1

    while i < len(intervals_a) and j < len(intervals_b):
        a = intervals_a[i]
        b = intervals_b[j]
        print("hello")
        print(a)
        print (b)
        # check if a lies within b
        a_overlaps_b =  a[start] >= b[start] and a[start] <= b[end]

        # check if b lies within a
        b_overlaps_a =  b[start] >= a[start] and b[start] <= a[end]

        if (a_overlaps_b or b_overlaps_a):
            overlapped = [max(a[start],b[start]), min(a[end], b[end])]
            result.append(overlapped)

        #move to the next one finishing first
        if a[end] < b[end]:
            i += 1
        else:
            j += 1
        
    return result

a = [[0,2],[5,10],[13,23],[24,25]]
b = [[1,5],[8,12],[15,24],[25,26]]
print(intersection(a,b))