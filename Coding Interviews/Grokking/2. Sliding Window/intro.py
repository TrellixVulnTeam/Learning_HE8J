# sample input = [1,3,2,6,-1,4,1,8,2]
# find averages of subarray - 5

def find_average_of_subarray_of_size(K, array) :
    window_sum = 0.0
    window_start = 0

    result = []
    for windowEnd in range (len(array)) :
        window_sum += array[windowEnd]

        #slide when index is greater than 4 (0,1,2,3,4)
        if windowEnd >= K - 1 :
            result.append(window_sum / K)
            window_sum -= array[window_start]
            window_start += 1
    
    return result

def main():
    print(find_average_of_subarray_of_size(5, [1,3,2,6,-1,4,1,8,2]))

if __name__ == "__main__":
    main()