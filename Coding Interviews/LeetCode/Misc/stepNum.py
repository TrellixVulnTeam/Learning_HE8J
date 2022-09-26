# import math
from collections import deque
# def stepnum(A, B):
#     nA = len(str(A))
#     nB = len(str(B))

#     answers = []
#     if A < 10:
#         answers += [str(i) for i in range(A, 10)]
#         A = 10
#         nA = len(str(A))
    
  
#     def dfs(currentStr, position):
#         lastDigit = currentStr[-1]
#         nextDigits = upOrDown(int(lastDigit))
#         if position == nA -1 :
#             answers.append(currentStr)
#         for nextDigit in nextDigits:
#             nextDigit = str(nextDigit)
#             newNumber = currentStr + nextDigit
#             actualNewNum = int(newNumber +"0"*(nA-2-position))
#             print(f'hello {(nA-2-position)}')
#             print(actualNewNum)
#             if actualNewNum >= A and int(newNumber +"0"*(nA-2-position)) < B:
#                 dfs(newNumber, position + 1)
#         return 
        
        
#     def upOrDown(num):
#         if num == 0:
#             return [1]
#         if num == 9:
#             return [8,10]
#         else:
#             return [num - 1, num + 1]
            
#     i = int(str(A)[0])
#     while int(str(i) +"0"*(nA-1)) < B:
#         dfs(str(i), 0)
#         i += 1
        
#     return answers

# print(stepnum(50,1000))


# def stepnumCorrect(n,m):
#     ans = []
#     def dfs(currentNum):
#         if currentNum >= n and currentNum <= m:
#             ans.append(currentNum)
#         if currentNum == 0 or currentNum > m:
#             return

#         lastDigit = currentNum % 10
#         nextNumA = currentNum*10 + lastDigit+1
#         nextNumB = currentNum*10 + lastDigit-1

#         if lastDigit == 0:
#             dfs(nextNumA)
#         elif lastDigit == 9:
#             dfs(nextNumB)
#         else:
#             dfs(nextNumB)
#             dfs(nextNumA)
#         return

#     for i in range(10):
#         dfs(i)
#     return ans

# print(stepnumCorrect(0,99))


def stepnumBFS(n,m):
    ans = []
    queue = deque([i for i in range(1,10)])
    if n == 0:
       ans.append(0)
    while queue:

        currentNum = queue.popleft()
        
        if currentNum >= n and currentNum <= m:
            ans.append(currentNum)
        if currentNum > m:
            break
        
        lastDigit = currentNum % 10
        nextNumA = currentNum*10 + lastDigit+1
        nextNumB = currentNum*10 + lastDigit-1

        if lastDigit == 0:
            queue.append(nextNumA)
        elif lastDigit == 9:
            queue.append(nextNumB)
        else:
            queue.append(nextNumB)
            queue.append(nextNumA)

    return ans

print(stepnumBFS(0,99))