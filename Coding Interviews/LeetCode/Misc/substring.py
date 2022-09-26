# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    n = len(S)
    currentChar = S[0]
    temp_count = 0
    ans = 0
    for i in range(0,n):
        if S[i] == currentChar:
            temp_count += 1
        else:
            
            ans += temp_count * (temp_count + 1) /2
            currentChar = S[i]
            #reset back to 1
            temp_count  = 1
            
            
    ans += (temp_count * (temp_count + 1)) /2
        
    return int(ans)

    
print(solution('zzzyz'))

        
