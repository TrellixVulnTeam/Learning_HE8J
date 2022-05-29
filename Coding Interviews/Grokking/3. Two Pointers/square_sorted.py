def squares_sorted(arr):
    
    left, right = 0, len(arr)
    squares = [0 for x in range (len(arr))]
    highest_square_index = len(arr) - 1 
    while left <= right :
        left_square = arr[left] * arr[left]
        right_square = arr [right]* arr [right]
        if (left_square >= right_square):
            squares[highest_square_index] = left_square
            left += 1
        else:
            squares[highest_square_index] = right_square
            right -= 1
        highest_square_index -= 1
    
    return squares