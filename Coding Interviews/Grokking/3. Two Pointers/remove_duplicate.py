def remove_duplicate(arr):

    #start with index 1 
    next_non_duplicate = 1

    i = 1
    while i < len(arr):
        #they start with pointing at the same place (second), then if the first element issame asfirst, nothing happens
        #if different, replace second wth second, which is also same
        if arr[next_non_duplicate - 1 ] != arr[i]:
            arr[next_non_duplicate] = arr [i]
            next_non_duplicate += 1

        #basially the idea is iterate through the list, then only move the next_non_duplicate once we replace it with a unique char.


    
    