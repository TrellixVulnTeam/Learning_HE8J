from collections import deque

def abbreviation(word):
    initial = ["", 0,0]
    substring, startIndex, count = 0, 1, 2
    queue = deque()
    queue.append(initial)
    result = []
    while queue:
        current = queue.popleft()
        
        if current[startIndex] == len(word):
            if current[count] > 0: 
                current[substring] = current[substring]+ str(current[count])
            result.append(current[substring])
        
        else :
            # either we continue with the count, meaning dont add the character yet
            queue.append([current[substring] , current[startIndex]+1, current[count] + 1])

             #or if we have a count that's more than zero, we add the number, and add the word char
            if current[count] > 0: 
                current[substring] = current[substring] + str(current[count])

            queue.append([current[substring] + word[current[startIndex]], current[startIndex] + 1, 0])

    return result

print(abbreviation("hello"))