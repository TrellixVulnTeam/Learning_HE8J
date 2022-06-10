#happy number
# those that are not will eventually be stuck inside a loop like  89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
# find the square sum, slow and fast
# because we know eventually they will meet if its a loop, then when fast is equal to slow, then there's a loop

def find_square_sum(num) :
    _sum = 0
    while (num > 0):
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum

def isHappyNumber(num) :
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))
        # it will be equal eventually, either both becomes 1, or it will meet somewhere in the loop
        if (slow == fast):
            break
        return slow == 1

#need look at time complexity